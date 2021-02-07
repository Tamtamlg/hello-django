from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello Django</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')

def contacts(request):
    return HttpResponse('<h1>Contacts</h1>')

def products(request, productid):
    output = '<h1>Product № {0}</h1>'.format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = '<h1>User</h1><h2>id: {0} name: {1}</h2>'.format(id, name)
    return HttpResponse(output)

def queryparams(request, productid):
    category = request.GET.get('cat', '')
    output = '<h1>Product № {0}</h1><h2>Category: {1}</h2>'.format(productid, category)
    return HttpResponse(output)