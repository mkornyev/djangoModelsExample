from django import forms

from django.contrib.auth.models import User
from models import *


class CreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = (
            'created_by',
            'creation_time',
            'updated_by',
            'update_time',
        )


class EditForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = (
            'created_by',
            'creation_time',
            'updated_by',
        )
        widgets = {
            'update_time': forms.HiddenInput(),
        }

