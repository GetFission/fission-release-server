from django.http import JsonResponse
from projects import models as project_models

import threading
from django.db import transaction

lock = threading.Lock()

def register_client(project, uid, version):
    c, created = project_models.ProjectClient.objects.get_or_create(uid=uid)
    c.project = project
    c.last_version_seen = version
    c.save()  # Save to update the last seen time stamp via auto_add_now
    return (c, created)


def update_result_for_release(release):
    """
    {
        'files': [{
            'url': 'http://localhost:8005/v6/electron-updater-example-0.6.0-mac.zip',
            'sha512': 'Sby01m3bYYslcBqqXVD4bE07eM0OjxQDJLnC3o+FJu4m7ohmxmVl65Epq13etYPQzzHJx+pTbJ1uQDCTAImDUA==' }
        ],
        'version': '0.6.0',
        'releaseDate': '2018-01-16T20:52:11.688Z'
    }
    """

    release_files = [release.get_darwin_release_files() or []]

    res = {
        'version': release.version,
        'releaseDate': release.created,
        'files': release_files
    }
    return res

def get_update_info(client_info):
    """Given a user and  app update URL, returns
    """
    # Notes: https://github.com/Squirrel/Squirrel.Mac#update-server-json-format
    # return {
    #     'url': 'https://gef-test.s3.amazonaws.com/electron-updater-example-0.6.0-mac.zip',
    #     'version': '0.6.0',
    #     'pub_date': 123
    # }

    project_key = client_info.get('project_key')
    project = project_models.Project.objects.get(api_key=project_key)

    # Don't send update clients never yet seen before

    res = None

    client, registered = register_client(project, client_info.get('uid'), client_info.get('version'))
    if registered:
        return {}

    release_rule = project.release_rules.all().order_by('release__version').first()

    # Note: this needs to be filtered by OS
    population_count = project.clients.all().count()
    population_with_version = project.clients.filter(last_version_seen=release_rule.release.version).count()
    current_distrib_percent = (population_with_version / float(population_count)) * 100
    print('actual', current_distrib_percent, 'but desired distribution', release_rule.darwin_percent)
    if current_distrib_percent >= release_rule.darwin_percent:
        print('sending over nothing')
        res =  {}
    else:
        update_result =  update_result_for_release(release_rule.release)
        client.last_version_sent = update_result.get('version')
        client.save()
        res = update_result
    return res



def get_client_info(request):
    client_info = {
      'uid': request.GET.get('uid'),
      'project_key': request.GET.get('projectKey'),
      'sysarch': request.GET.get('sysarch'),
      'version': request.GET.get('version'),
      'channel': request.GET.get('channel'),
      'os': request.GET.get('os') or 'mac'
    }
    return client_info


def serve_update(request):
    update_info = get_update_info(get_client_info(request))
    return JsonResponse(update_info)


def UnhandledURL(request, *args, **kwargs):
    print('Request received')
    # print(request.path)
    # print('Args', args)
    # print('Kwargs', kwargs)
    print(request.GET)
    return serve_update(request)
    # return HttpResponse('We tried...')
