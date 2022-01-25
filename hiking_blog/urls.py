"""hiking_blog URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BlogsView.as_view(), name='blog_list'),
    path('filter/', views.FilterBlogsView.as_view(), name='filter'),
    path('blog/', include('blog.urls')),
    path("blog/<int:pk>/update/", views.BlogUpdateView.as_view(), name='update'),
    path("blog/<int:pk>/delete/", views.BlogDeleteView.as_view(), name='delete'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Blogs
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('myblogs/', views.MyBlogsView, name='myblogs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
