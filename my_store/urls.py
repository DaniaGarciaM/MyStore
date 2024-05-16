from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def hello(request):
    return HttpResponse('<H1>HOLA 💗</H1>')

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
]
