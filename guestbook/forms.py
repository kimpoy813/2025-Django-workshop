from django import forms

from . import models

class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = models.Guest
        # fields = "__all__"
        fields = ['message']
        
