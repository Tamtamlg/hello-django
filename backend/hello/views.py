from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse('<h2>Hello {0}</h2>'.format(name))
    else:
        user_form = UserForm()
        data = {
            'header': 'Hello from Django template',
            'message': 'lorem ipsum dalor...',
            'n': 5,
            'langs': ["English", "German", "French", "Spanish", "Chinese"],
            'form': user_form,
        }
        return render(request, 'hello/index.html', context=data)

# def about(request):
#     return HttpResponse('<h1>About</h1>')

# def contacts(request):
#     return HttpResponse('<h1>Contacts</h1>')

# def products(request, productid):
#     output = '<h1>Product № {0}</h1>'.format(productid)
#     return HttpResponse(output)

# def users(request, id, name):
#     output = '<h1>User</h1><h2>id: {0} name: {1}</h2>'.format(id, name)
#     return HttpResponse(output)

# def queryparams(request, productid):
#     category = request.GET.get('cat', '')
#     output = '<h1>Product № {0}</h1><h2>Category: {1}</h2>'.format(productid, category)
#     return HttpResponse(output)

# def news(request):
#     return HttpResponseRedirect('/about')

# def details(request):
#     return HttpResponsePermanentRedirect('/')