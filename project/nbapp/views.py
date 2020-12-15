from django.shortcuts import render
# from nbapp.models import *
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from .models import URL

class Home(TemplateView):
    template_name = 'home.html'
    
@csrf_exempt
def shorturl(request):
    if request.method == 'POST':
        data = request.POST 
        given_url = data['entered_url']
        base_url = "http://127.0.0.1:8000/"
        try:
            url,created = URL.objects.get_or_create(
                full_url = data['entered_url'],
                created_by = request.user
            )
            url.save()
            short_url = base_url + url.url_hash
        except:
            pass
    context_data = dict()
    context_data['short_url'] = short_url
    context_data['given_url'] = given_url
    return render(request,'shorturl_success.html',context_data)


