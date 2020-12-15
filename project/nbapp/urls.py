
from django.urls import path,include
from .views import shorturl

urlpatterns = [
    
    path('short_url/', shorturl),
    
]
