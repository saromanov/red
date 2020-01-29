from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Person
from django.contrib.auth.mixins import LoginRequiredMixin

class PersonDetailView(DetailView):
    template_name = 'teams/person.html'
    model = Person

class LoginView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


def get_persons(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render('request', 'persons.html', context)

def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    context = {
        'person': person,
    }
    return render('request', 'person.html', context)

