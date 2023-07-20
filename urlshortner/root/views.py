from django.shortcuts import render, redirect
from django.http import HttpResponse
from root.models import Url


def creatURL(req):
    if req.method == 'POST':
        full_url = req.POST.get('full_url')
        objt=Url.Create(full_url)
        return render(req, 'root/index.html', {
            'full_url': objt.full_url,
            'short_url': req.get_host()+'/'+objt.short_url
        })
    
    return render(req, 'root/index.html') 

def routeToURL(req, key):
        try:
            obj = Url.objects.get(short_url=key)
            return redirect(obj.full_url)
        except:
            return redirect(creatURL)    
