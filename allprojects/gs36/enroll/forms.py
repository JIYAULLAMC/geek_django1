from django import forms

from django.core import validators

#cutstom validators

def name_starts_with_s(name):
    if name[0] != 's':
        raise forms.ValidationError("Name should start with s")


class Register(forms.Form):
    # name = forms.CharField(min_length=5, empty_value="ccccccc", error_messages={"min_length": "Dear please enter valid name more than 5 letters :) love you"})
    # name = forms.DecimalField(min_value=0, max_value=100, max_digits=4, decimal_places=2)

    # exatra validations
    name = forms.CharField(validators=[validators.MaxLengthValidator(5), name_starts_with_s])
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    # exatra validations

    # def clean_name(self):
    #     form_name = self.cleaned_data['name']
    #     if not form_name.istitle():
    #         raise forms.ValidationError(f"Enter Copitalized data {form_name.title()}")

    #     return form_name


    # for clean method to validata whole form
    # def clean(self):
    #     cleaned_data = super().clean()
    #     form_name =  cleaned_data['name']
    #     if not form_name.istitle():
    #         raise forms.ValidationError(f"Enter Copitalized data {form_name.title()}")
    

    # for clean method to validata whole form
    # comaparing both passwords
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data['password1']
        pwd2 = cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError(f"passwoeds are not mathing {pwd1}  {pwd2}" )

 