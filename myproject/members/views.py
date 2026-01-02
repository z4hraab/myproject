#Django views are Python functions that take http requests and return http response, like HTML documents.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def Members(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context={
      'mymembers': mymembers
    }
    return HttpResponse(template.render(context,request))

