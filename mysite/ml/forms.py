from django import forms
from ml.models import Student

from ml.models import School


class Studentform(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'school_id']

        # school_id = forms.ModelChoiceField(queryset=models.School.objects.all(
        # ), widget=forms.Select(attrs={'class': 'hidden'}))

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control is-valid oval_border', 'placeholder': 'Enter your First Name', 'id': 'form-first_name', }),

            'last_name': forms.TextInput(attrs={'class': 'form-control is-valid oval_border', 'placeholder': 'Enter your Last Name', 'id': 'form-last_name', }),


            'school_id': forms.Select(attrs={'class': 'form-control is-valid oval_border'})
        }


class Schoolform(forms.ModelForm):

    class Meta:
        fields = ["name"]
        model = School
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control is-valid oval_border', 'placeholder': 'Enter your School Name', 'id': 'form-school_name', }),
        }
