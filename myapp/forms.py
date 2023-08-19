from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = "__all__"
      widgets = {'blog_post': SummernoteWidget()}