from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('enter'  )
    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    return HttpResponse ('this is right')

def insert_Webpage(request):
    tn=input('enter the topic ')
    TO=Topic.objects.get_or_create(topic_name=tn) [0]

    name1=input('enter the player')
    url1=input('enter the url')
    WO=Webpages.objects.get_or_create(topic_name=TO,name=name1,url=url1)[0]

    return HttpResponse('web page has been updated')

def insert_access(request):
    tn=input('enter the topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    name1=input('enter the player')
    url1=input('enter the url ')

    WO=Webpages.objects.get_or_create(topic_name=TO,name=name1,url=url1)[0]

    author=input('enter the author ')
    date=input('enter the date ')
    A0=AccessRead.objects.get_or_create(name=WO,Author=author,Date=date) [0]

    return HttpResponse('the access read succesful')