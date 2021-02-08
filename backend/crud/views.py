from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Person

def index(request):
    people = Person.objects.all()
    return render(request, 'crud/index.html', {'people': people})

def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/') # TODO: fix
        else:
            return render(request, 'crud/edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")