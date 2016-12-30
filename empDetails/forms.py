'''
Created on 30-Dec-2016

@author: sachin
'''
from django import forms
from .models import EmpDetailsModel


class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpDetailsModel
        fields = [
            "empName",
            "deptName",
            "file",
            "tagName",
            ]