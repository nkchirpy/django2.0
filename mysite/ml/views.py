from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models
from .forms import Studentform, Schoolform
# Create your views here.


def detailview(request):
    schools = models.School.objects.all()
    students = models.Student.objects.all()
    return render(request, 'detail.html', {'schools': schools, 'students': students})


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
