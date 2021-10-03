from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class CategoryModel(models.Model):
    title = CharField(max_length=100,null=True,blank=True)
    

class StyleModel(models.Model):
    name = CharField(max_length=100,null=True,blank=True)

