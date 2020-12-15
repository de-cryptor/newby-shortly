from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

class Home(TemplateView):
    template_name = 'home.html'
    
@csrf_exempt
def shorturl(request):
    return render(request,'shorturl_success.html')
