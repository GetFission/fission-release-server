from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def get_update_info(client_info):
    """Given a user and  app update URL, returns
    """
    # Notes: https://github.com/Squirrel/Squirrel.Mac#update-server-json-format
    return {
        'url': 'https://gef-test.s3.amazonaws.com/electron-updater-example-0.6.0-mac.zip',
        'version': '0.6.0',
        'pub_date': 123
    }
    return {
        'files': ['https://gef-test.s3.amazonaws.com/electron-updater-example-0.6.0-mac.zip'],
        'version': '0.6.0',
        'releaseDate': '2018-01-16T20:52:11.688Z'
    }


def get_client_info(request):
    client_info = {
      'user_id': request.GET.get('userId'),
      'project_key': request.GET.get('projectKey'),
      'sysarch': request.GET.get('sysarch'),
      'version': request.GET.get('version'),
      'channel': request.GET.get('channel'),
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
