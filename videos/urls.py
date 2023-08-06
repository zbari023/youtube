from .views import video_list
from django.urls import path


urlpatterns = [
    path('', video_list),
    
]