from django.urls import path

from .import views
from .views import PostListView , PostDetailView , PostCreateView , PostUpdateView , UserPostListView , PostDeleteView
urlpatterns = [
    path('', views.PostListView.as_view(template_name='blog/home.html'), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(template_name='blog/post_detail.html'), name='blog-post-detail'),
    path('post/new/', views.PostCreateView.as_view(template_name='blog/post_form.html'), name='blog-post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(template_name='blog/post_form.html'), name='blog-post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-post-delete'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='blog-user-posts'),

]