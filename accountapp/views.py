from django.contrib.auth import login
from django.db import models
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountUpdateForm
from .models import HelloWorld
from django.contrib.auth.decorators import login_required

from django.urls import reverse,reverse_lazy


from django.utils.decorators import method_decorator
from .decorators import account_ownership_required

has_ownership = [account_ownership_required,login_required]

# Create your views here.
@login_required
def hello_world(request):

        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            context = {
                'hello_world_list' : hello_world_list
            }
            return render(request,'accountapp/helloworld.html',context)
    


class AccountCreateView(CreateView):
        model = User
        form_class = UserCreationForm
        #reverse_lazy는 클래스형에서 사용함 reverse는 함수형에서 사용
        success_url = reverse_lazy('accountapp:hello_world')
        template_name ='accountapp/create.html'

class AccountDetailView(DetailView):
        model = User
        #다른 사람 페이지 접속했을때 그 사람 정보 확인
        #context_object_name 속성을 사용하면 변수를 사용할 수 있다.
        context_object_name = 'target_user'
        template_name ='accountapp/detail.html '

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountUpdateView(UpdateView):
        model = User
        form_class = AccountUpdateForm
        context_object_name = 'target_user'
        #reverse_lazy는 클래스형에서 사용함 reverse는 함수형에서 사용
        success_url = reverse_lazy('accountapp:hello_world')
        template_name ='accountapp/update.html'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountDeleteView(DeleteView):
        model = User
        context_object_name = 'target_user'
        success_url = reverse_lazy('accountapp:login')
        template_name = 'accountapp/delete.html'

