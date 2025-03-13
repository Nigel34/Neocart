
from django.contrib import admin
from django.urls import path
from NeoApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('blogs/',views.blog_details,name='blogs'),
    path('starter/',views.starter,name='starter'),
    path('portfolio/',views.portfolio,name='portfolio'),


]
