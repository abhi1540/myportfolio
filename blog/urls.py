from django.contrib import admin
from django.urls import path,re_path
from blog import views

app_name = 'blog'
urlpatterns = [

    path('', views.AllBlog.as_view(), name='home'),
    path('aboutme/', views.about_me, name='about'),
    path('<tag>/', views.TagDetailView.as_view(), name='categories'),
    path('<tag>/<slug>/', views.SlugDetailView.as_view(), name='detail')

]
