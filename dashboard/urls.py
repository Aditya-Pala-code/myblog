from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-post/', views.add_post, name='add_post'),
    path('update-post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('view-post/<int:post_id>/', views.view_post, name='view_post'),
]