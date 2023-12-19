from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    username = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget = forms.TextInput(attrs={
                "placeholder":"username",
                "name":"username",
                "class":"form-control my-2 mx-1",
                "type":"text",
                })
            )

    email = forms.EmailField(
        label="",
        required=True,
        widget = forms.TextInput(attrs={
            "placeholder":"Email",
            "type":"email",
            "name":"email",
            "class":"form-control my-2 mx-1",
            })
        )

    password1 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"password",
            "type":"password",
            "name":"password1",
            "class":"form-control my-2 mx-1",
            })
        )

    password2 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"confirm password",
            "type":"password",
            "name":"password1",
            "class":"form-control my-2 mx-1",
            })
        )
    class Meta:
        model = User
        fields = ("username","email")
