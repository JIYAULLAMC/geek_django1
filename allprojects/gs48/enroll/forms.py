
from django import forms

from enroll.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
        labels = {"name": "Enter the name", 'password': "Enter the password"}
        error_messages = {
            "name": {
                "required": "Nam likhana jarori hai"
            },
            "email": {
                "required": "Email likhana jarori hai"
            }
        }
        widgets = {
            'password': forms.PasswordInput,
            # 'name':forms.Textarea,
        }
