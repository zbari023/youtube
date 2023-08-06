from .views import video_list , video_detail
from django.urls import path


urlpatterns = [
    path('', video_list),
    path('<int:video_id>',video_detail),
    
]