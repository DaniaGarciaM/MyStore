from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def hello(request):
    return HttpResponse('<H1>HOLA 💗</H1>')

def multiply(request, num):
    html = f'<h1>Tabla del {num} ❎</h1>'
    for i in range(1,10):
        html += f'<p>{num} * {i} = {i*num}</p>'
    return HttpResponse(f'<h3>{html}</h3>')

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    #Ruta para enviar parámetros
    path('table/<int:num>', multiply, name='multiply')
]
