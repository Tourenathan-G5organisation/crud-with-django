from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, context, RequestContext
from django.shortcuts import render_to_response
from .models import Person

# Create your views here.

def index(request):
    people = Person.objects.all();

    return render_to_response('crud/index.html',{'people':people})

def inset(request):
    #if this is a post request we insert the person
    if request.method == 'POST':
        p = Person(
            name = request.POST['name'],
            phone = request.POST['phone'],
            age = request.POST['age']
        )
        p.save()

    t = loader.get_template('crud/insert.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))


def delete(request, person_id):
    p = Person.objects.get(pk=person_id)
    p.delete()
    return  HttpResponseRedirect('/')

#Edit function
def edit(request, person_id):
    p = Person.objects.get(pk=person_id)
    if request.method == 'POST':
        p.name = request.POST['name']
        p.phone = request.POST['phone']
        p.age = request.POST['age']
        p.save()

    t = loader.get_template('crud/insert.html')
    c = RequestContext(request, {'person':p})
    return HttpResponse(t.render(c))

