from django.db import models
import hashlib 
# Create your models here.

class Url(models.Model):

    full_url =  models.CharField(unique=True,max_length=1000)
    short_url = models.CharField(unique=True,max_length=20)
    
    def __str__(self):
        return self.full_url
    
    @classmethod 
    def Create(self, full_url):
        temp = hashlib.md5(full_url.encode()).hexdigest()[:5]
        try:
            obj=self.objects.create(full_url=full_url , short_url=temp  )
        except:
            obj=self.objects.get(full_url=full_url)
        return obj