# from __future__ import all_feature_names
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


books=[
    {"bname":"Alchemist","aname":"Paulo Coelho","price":"235"},
    {"bname":"Death of a city","aname":"Amrita Pritam","price":"245"},
    {"bname":"Apple Cart","aname":"George Bernard Shaw","price":"255"},
    {"bname":"Autobiography of an Unknown Indian","aname":"Nirad C. Choudhury","price":"265"}

    
]
class Books(models.Model):
    bname=models.CharField(max_length=200)
    aname=models.CharField(max_length=150)
    price=models.IntegerField(default=100)



