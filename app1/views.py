from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView

from .forms import PersonForm
from .models import Person

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')
    template_name = 'home.html'
    success_url = '/'


def home(request):
    data = Person.objects.all()
    context = {
        'data': data,
    }
    return render(request,'test.html',context)


def delete(request,id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('home')

