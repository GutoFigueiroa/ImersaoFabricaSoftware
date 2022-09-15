from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chiclete(request):
    
    return render(request, template_name='blog/home.html')

def jujuba(request):
    html = "<html><body><h1>Tome Jujuba</h1></body></html>"
    return HttpResponse(html)