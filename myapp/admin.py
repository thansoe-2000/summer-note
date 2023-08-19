from django.contrib import admin
from . models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


admin.site.register(Category)

class PostAdmin(SummernoteModelAdmin):
     summernote_fields = ('blog_post')
admin.site.register(Post, PostAdmin)