from django.forms import Form, CharField, PasswordInput, DateInput, Textarea, ModelForm, Select, ChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Quote

class LoginForm(Form):
    username = CharField(max_length=50)
    password = CharField(max_length=50, widget=PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                   'email',
                   'password1',
                   'password2'
            ] 
        
class Author_Form(ModelForm):
    name = CharField(max_length=40)
    born_date = CharField(max_length=250,widget=DateInput)
    born_location = CharField(max_length=40)
    decsription = CharField(widget=Textarea)
    
    class Meta:
        model = Author
        fields = ["name",
                "born_date",
                "born_location",
                "decsription"
                ]
        
class Quote_Form(ModelForm):
    class Meta:
        model = Quote
        fields = [
            'text',
            'author'
        ]

class Reset_Form(Form):
    email = CharField()
