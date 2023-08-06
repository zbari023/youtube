from django.shortcuts import render, redirect
from .models import  Video, Comment 
from .forms import PostForm

# Create your views here.

def video_list(request):
    data = Video.objects.all()
    return render(request,'videos/index.html',{'data':data})