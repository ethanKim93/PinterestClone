
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from articleapp.views import ArticleCreateView,ArticleDetailView,ArticleUpdateView,ArticleDeleteView

app_name = 'articleapp'
urlpatterns = [
    #TemplateView만 지정해주면 알아서 됨
    path('list/',TemplateView.as_view(template_name='articleapp/list.html'),name='list'),
    path('create/',ArticleCreateView.as_view(),name='create'),
    path('detail/<int:pk>',ArticleDetailView.as_view(),name='detail'),
    path('update/<int:pk>',ArticleUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',ArticleDeleteView.as_view(),name='delete'),

] 

