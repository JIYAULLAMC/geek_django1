from django import forms





class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)



#how tho add the bootstrap

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","email", "password"]
        widgets = {"name":forms.TextInput(attrs={"class": "mybootclass"}),
        "password":forms.PasswordInput(attrs={"class":"mypass"})}