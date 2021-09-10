from django import forms
from firstapp.models import TestData

# Regular Form
class CreateForm(forms.Form):
    # fieldName = forms.FieldType(options)
    studentName = forms.CharField()
    courseName = forms.CharField()
    Email = forms.EmailField()

# MODEL FORM
class CreateModelForm(forms.ModelForm):
    # modify your fields here

    class Meta:
        model = TestData
        # fields = ['StudentName','CourseName'] # make specific fields visible
        # exclude = ['Email'] # make fields invisible
        fields = '__all__' # make all fields visible













