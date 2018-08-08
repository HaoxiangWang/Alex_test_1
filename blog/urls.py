from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url('post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    url('', views.index, name='index'),
]
