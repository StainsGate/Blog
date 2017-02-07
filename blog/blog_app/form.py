from django import forms
from blog_app.models import Blog,Comment
from django_summernote.widgets import SummernoteWidget



class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    content = forms.CharField(widget=SummernoteWidget())
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    comments = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model = Blog
        fields = ('title','content',)