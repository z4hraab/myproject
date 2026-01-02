#Django views are Python functions that take http requests and return http response, like HTML documents.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Members(request):
    template=loader.get_template('myfirst.html')
    return HttpResponse(template.render())

