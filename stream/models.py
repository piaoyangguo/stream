#coding: utf8
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(u"姓名", max_length=200)
    age = models.IntegerField(u'年龄', default=0)