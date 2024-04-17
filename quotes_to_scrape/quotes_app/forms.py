from django.forms import ModelForm, CharField, Form
# from django.contrib.auth import get_user_model
# from .models import User


class LoginForm(Form):
    name = CharField(required=True)
    email = CharField(required=True)

   