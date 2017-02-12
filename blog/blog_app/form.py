from django import forms
from blog_app.models import Blog,Comment,Userprofile
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


class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=200)
    publisher = forms.CharField(max_length=200)

    class Meta:
        model = Comment
        fields = ('publisher','content',)

class UserProfileForm(forms.ModelForm):
    logo = forms.ImageField()
    points = forms.IntegerField(widget=forms.HiddenInput(),initial=10)

    class Meta:
        model = Userprofile
        fields = ('logo',)