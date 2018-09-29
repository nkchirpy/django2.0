from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models
from .forms import Studentform, Schoolform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import requests

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form':form}

    return render(request, 'registration/register.html', context)



def detailview(request):
    schools = models.School.objects.all()
    students = models.Student.objects.all()
    response = requests.get('https://api.printful.com/countries')
    data = response.json()
    return render(request, 'detail.html', {'schools': schools, 'students': students,'ip': data})


class Index(TemplateView):
    template_name = 'index.html'


class Studentview(CreateView):

    model = models.Student
    form_class = Studentform
    template_name = 'student.html'
    success_url = reverse_lazy('student')


class Schoolview(CreateView):

    model = models.School
    form_class = Schoolform
    template_name = 'school.html'
    success_url = reverse_lazy('school')

class Schooldeleteview(DeleteView):
    model = models.School
    template_name = 'school_confirm_delete.html'
    success_url = reverse_lazy('detail')


class Schoolupdateview(UpdateView):
    model = models.School
    fields = ['name']
    template_name = 'school_form.html'
    success_url = reverse_lazy('detail')



class Success_view(TemplateView):
    template_name = "succeess.html"
# from myapp.forms import ContactForm
#


# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)
