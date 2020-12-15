from django.db import models
from hashlib import md5
from django.contrib.auth.models import User
# Create your models here.

class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} >> {}".format(self.full_url,self.url_hash)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)
    
    
class URLClickHistory(models.Model):
    url = models.ForeignKey(URL,blank=True,null=True,on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100,blank=True,null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    clicked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} >> {} >> {}".format(self.url.full_url,self.ip_address,self.location)
    
    
    
