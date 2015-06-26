from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, context, RequestContext
from django.shortcuts import render_to_response
from .models import Person

# Create your views here.

def index(request):
    return render_to_response('crud/index.html',{'message':'Hello world!'})

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
