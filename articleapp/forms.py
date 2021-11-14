from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))#높이가 자동으로 따라감
    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    class Meta:
        model = Article
        fields =['title','image','project','content']
