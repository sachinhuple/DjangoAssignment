from __future__ import unicode_literals

from django.db import models

# Create your models here.


class EmpDetailsModel(models.Model):
   
    empName = models.CharField(max_length=60)
    deptName = models.CharField(max_length=30)
    tagName = models.CharField(max_length=15)
    file = models.FileField(null=False,blank=False) 
           
