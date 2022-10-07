"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from blog import views as blog_views
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryCreateView,
    CategoryView,
)

urlpatterns = [
    # path('', blog_views.home, name = 'blog_home'),
    path('',PostListView.as_view(), name = 'blog_home'),
    # path('',AboutView.as_view(), name = 'blog_about'),
    path('about/', blog_views.about, name = 'blog_about'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('category/new/',CategoryCreateView.as_view(), name = 'category_form'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
]