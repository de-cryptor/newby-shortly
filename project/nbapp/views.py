from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json

class Home(TemplateView):
    template_name = 'home.html'
    
@csrf_exempt
def shorturl(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
    context_data = dict()
    context_data['short_url'] = "https://nbapp.com/gtyh567sd"
    return render(request,'shorturl_success.html',context_data)


