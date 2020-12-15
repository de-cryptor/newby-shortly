from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
import validators
import requests
from django.core import serializers
import traceback

class Home(TemplateView):
    template_name = 'home.html'
    
@csrf_exempt
def shorturl(request):
    context_data = dict()
    short_url = ""
    given_url = ""
    if request.method == 'GET':
        return render(request,'home.html',context_data)
    
    if request.method == 'POST':
        data = request.POST 
        given_url = data['entered_url']
        base_url = "https://immense-island-94283.herokuapp.com/"
        
        if validators.url(given_url):
            try:
                url,created = URL.objects.get_or_create(
                    full_url = data['entered_url'],
                )
                if not request.user.is_anonymous:
                    url.created_by = request.user
                url.save()
                short_url = base_url + url.url_hash
                
            except:
                print(traceback.format_exc(limit=None, chain=True))
        else:
            pass
    if not request.user.is_anonymous:
        print(request.user)
        created_urls = URL.objects.filter(created_by=request.user)
        context_data['created_urls']  = json.loads(serializers.serialize("json",created_urls))
    else:
        context_data['created_urls']  = []
    context_data['short_url'] = short_url
    context_data['given_url'] = given_url
    context_data['base_url'] = base_url
    print(context_data)
    return render(request,'shorturl_success.html',context_data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def url_redirect(request,url_hash):
    link = URL.objects.get(url_hash=url_hash)
    ip = get_client_ip(request)
    geo_url = "https://geolocation-db.com/json/{}&position=true".format(ip)
    response = requests.get(geo_url).json()
    print(response)
    url_access = URLClickHistory.objects.create(
        url=link,
        ip_address=ip,
        location=response['city']
    )
    link.clicked()
    return HttpResponseRedirect(link.full_url)