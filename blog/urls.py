from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="base"),
    path('post/<int:id>/', views.post_detail, name="post_detail"),
    path('about/',views.about,name="about"),
    path("blog/",views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
]