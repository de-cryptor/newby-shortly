
from django.urls import path,include
from .views import shorturl,url_redirect

urlpatterns = [
    
    path('short_url/', shorturl),
    # path('<str:url_hash>/', url_redirect),
    
]
