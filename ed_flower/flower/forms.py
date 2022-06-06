from .models import FlowerModel
from django import forms

class FlowerUpload(forms.ModelForm):
    class Meta:
        model = FlowerModel
        fields = ['image']