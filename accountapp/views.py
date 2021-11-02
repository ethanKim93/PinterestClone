from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse,reverse_lazy

# Create your views here.
def hello_world(request):
    return render(request,'accountapp/helloworld.html')


class AccountCreateView(CreateView):
        model = User
        form_class = UserCreationForm
        #reverse_lazy는 클래스형에서 사용함 reverse는 함수형에서 사용
        success_url = reverse_lazy('accountapp:hello_world')
        template_name ='accountapp/create.html'