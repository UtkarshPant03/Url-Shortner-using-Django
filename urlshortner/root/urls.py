
from django.urls import path
from root.views import creatURL, routeToURL

urlpatterns = [
    path('', creatURL),
    path('<slug:key>/', routeToURL)
]
