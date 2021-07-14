from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blog, name='all_blog'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
