from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from embed_video.admin import AdminVideoMixin
# Register your models here.
from .models import Video, Comment 






class VideoAdmin(SummernoteModelAdmin):
    list_display = ['author']
    list_filter = ['author']
    search_fields = ['author']
    summernote_fields = '__all__'
    
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Comment, VideoAdmin )
admin.site.register(Video , MyModelAdmin)