from django import forms
from .models import Video , Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'