from decimal import Decimal
import random

from django.conf import settings
from django.db import models

from django_extensions.db import models as dj_models

from projects import models as project_models


class Release(dj_models.TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(project_models.Project, blank=True, null=True)

    # Todo: investigate windows artifacts (nsis, squirrel, nuget, etc..)
    windows_artifact = models.FileField(null=True, blank=True)

    # Produced by electron builder. Mac zip-file is needed for auto-update
    darwin_zip = models.FileField(null=True, blank=True)
    darwin_zip_sha512 = models.TextField(blank=True, null=True)
    darwin_dmg = models.FileField(null=True, blank=True)
    darwin_dmg_sha512 = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_darwin_release_files(self):
        res = []
        if self.darwin_zip:
            res.append({
                'url': self.darwin_zip.url,
                'sha512': self.darwin_zip_sha512
            })
        if self.darwin_dmg:
            res.append({
                'url': self.darwin_dmg.url,
                'sha512': self.darwin_dmg_sha512
            })
        return res

    def __str__(self):
        return '<{}/{}/{}>'.format(self.project.name, self.version, self.name)

    def __repr__(self):
        return self.__str__()


class ReleaseRule(dj_models.TimeStampedModel):
    release = models.ForeignKey(Release, blank=True, null=True)
    project = models.ForeignKey(
        project_models.Project,
        blank=True, null=True,
        related_name='release_rules'
    )
    is_darwin = models.BooleanField(default=False)

    is_windows = models.BooleanField(default=False)
    is_linux = models.BooleanField(default=False)
    channel = models.CharField(max_length=255, blank=True, null=True)
    darwin_percent = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    windows_percent = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    linux_percent = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)

    def generate_members(self):
        """
        Generate a members list for each OS
        :return:
        """
        from projects.models import ProjectClient

        current_members = [
            member.project_client.uid
            for member in ReleaseMember.objects.filter(release_rule=self)
        ]
        project_members_count = ProjectClient.objects.count()
        if not project_members_count > 0:
            return
        release_rule_pop_percent  = len(current_members) / float(project_members_count)

        darwin_percent = self.darwin_percent / 100

        if release_rule_pop_percent < darwin_percent:
            # Expand rule members
            eligible_clients_ids = list(ProjectClient.objects.exclude(uid__in=current_members).values('id'))
            backfill_percent = (darwin_percent - Decimal(release_rule_pop_percent))
            backfill_pop_size = int(round(backfill_percent * project_members_count))
            print(f'Need to get {backfill_pop_size} to reach {darwin_percent}')
            random.shuffle(eligible_clients_ids)
            new_clients = eligible_clients_ids[:backfill_pop_size]
            print('Will create the following new clients', new_clients)
            ReleaseMember.objects.bulk_create([
                ReleaseMember(release_rule=self, project_client_id=client.get('id'))
                for client in new_clients
            ])
            print('new rule members generated')

    def is_promised_client(self, uid):
        release_members = ReleaseMember.objects.filter(release_rule=self, is_rolled_back=False)
        current_members = set([
            member.project_client.uid
            for member in release_members
        ])
        print('checking for', uid, 'in', current_members)
        return uid in current_members


class ReleaseMember(dj_models.TimeStampedModel):
    project_client = models.ForeignKey('projects.ProjectClient', related_name='members')
    release_rule = models.ForeignKey(ReleaseRule, related_name='members')
    is_rolled_back = models.BooleanField(default=False)

    def __str__(self):
        return '<RR {}/PC {}>'.format(self.release_rule.id, self.project_client.uid)

    def __repr__(self):
        return self.__str__()
