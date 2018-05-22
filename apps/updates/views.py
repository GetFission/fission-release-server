from django.http import JsonResponse
from projects import models as project_models

from glom import glom


def register_client(project, uid, version):
    c, created = project_models.ProjectClient.objects.get_or_create(uid=uid)
    c.project = project
    c.last_version_seen = version
    c.save()  # Save to update the last seen time stamp via auto_add_now
    return (c, created)


def update_result_for_release(release, platform):
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

    if platform == 'win32':
        release_files = [release.get_darwin_release_files() or []]
    elif platform == 'darwin':
        release_files = [release.get_windows_release_files() or []]
    else:
        raise Exception('Update Result requested for unsupported platform')

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

    res = {}

    client, registered = register_client(
        project, client_info.get('uid'), client_info.get('version'))
    if registered:
        return {}

    # TODO: if this release rule is not applicable then keep looking back
    release_rule = project.release_rules.all().order_by('release__version').first()

    # Note: this needs to be filtered by OS
    if release_rule.is_promised_client(client_info.get('uid')):
        print('True %%%%%')
        update_result =  update_result_for_release(release_rule.release)
        client.last_version_sent = update_result.get('version')
        client.last_version_sent_release_rule = release_rule
        client.save()
        res = update_result
    return res



def get_client_info(request):
    client_info_spec = {
      'uid': ('uid', lambda x: str(x)),
      'project_key': 'projectKey',
      'sysarch': 'sysarch',
      'version': 'version',
      'channel': 'channel',
      'platform': 'platform'
    }
    res = glom(request.GET, client_info_spec)
    import pdb; pdb.set_trace()

    return res


def serve_update(request):
    update_info = get_update_info(get_client_info(request))
    return JsonResponse(update_info)


# TODO: log calls to this endpoint
def update_view_func(request, *args, **kwargs):
    # print('Request received')
    # print(request.path)
    # print('Args', args)
    # print('Kwargs', kwargs)
    # print(request.GET)
    return serve_update(request)
    # return HttpResponse('We tried...')
