from django import forms



class Register(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    first_name = forms.CharField(widget=forms.Textarea(attrs={"class":"myclass"}))


    