from dataclasses import fields
from pyexpat import model
from django import forms

from booklist.models import Books
from django.contrib.auth.models import User

class BookForm(forms.Form):
    bname=forms.CharField(label="Book name",required=True)
    aname=forms.CharField(label="Author name",required=True)
    price=forms.IntegerField(label="price",required=True)


class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))






