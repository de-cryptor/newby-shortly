from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponsePermanentRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import URL
import validators

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
        base_url = "http://127.0.0.1:8000/"
        
        if validators.url(given_url):
            try:
                url,created = URL.objects.get_or_create(
                    full_url = data['entered_url'],
                    created_by = request.user
                )
                url.save()
                short_url = base_url + url.url_hash
            except:
                pass
        else:
            pass
    context_data['short_url'] = short_url
    context_data['given_url'] = given_url
    return render(request,'shorturl_success.html',context_data)


def url_redirect(request,url_hash):
    link = URL.objects.get(url_hash=url_hash)
    link.clicked()
    return HttpResponsePermanentRedirect(link.full_url)