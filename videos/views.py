from django.shortcuts import render, redirect
from .models import  Video, Comment 
from .forms import PostForm

# Create your views here.

def video_list(request):
    data = Video.objects.all()
    return render(request,'videos/index.html',{'data':data})



def video_detail(request,video_id):
    data = Comment.objects.get(id=video_id)
    return render(request,'videos/detail.html',{'data':data})