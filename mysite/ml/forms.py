from django import forms
from ml.models import Student

from ml.models import School


class Studentform(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'state', 'school_id']

        # school_id = forms.ModelChoiceField(queryset=models.School.objects.all(
        # ), widget=forms.Select(attrs={'class': 'hidden'}))

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control is-valid oval_border', 'placeholder': 'Enter your Student Name', 'id': 'form-first_name', }),

            'state': forms.TextInput(attrs={'class': 'form-control is-valid oval_border', 'placeholder': 'Enter your State', 'id': 'form-last_name', }),


            'school_id': forms.Select(attrs={'class': 'form-control is-valid oval_border', 'string': 'Schools'})
        }

    def __init__(self, *args, **kwargs):

        super(Studentform, self).__init__(*args, **kwargs)
        self.fields['school_id'].label = "Schools"
        self.fields['name'].label = "Student Name"

class Schoolform(forms.ModelForm):

    class Meta:
        fields = ["name"]
        model = School
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control is-valid oval_border', 'placeholder': 'Enter your School Name', 'id': 'form-school_name', }),
        }
