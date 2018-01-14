from django.shortcuts import render
from django.http import HttpResponse


def UnhandledURL(request, *args, **kwargs):
  print('Request received')
  print(request.path)
  print('Args', args)
  print('Kwargs', kwargs)
  print(request.GET)
  return HttpResponse('We tried...')
