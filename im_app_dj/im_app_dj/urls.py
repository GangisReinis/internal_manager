"""im_app_dj URL Configuration

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
from django.urls import path
from django.views.generic.edit import DeleteView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update/', views.UpdateBlog.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', views.DeleteBlog.as_view(), name='blog-delete'),
    path('blog/create-new/', views.CreateBlog.as_view(), name='blog-create'),
]

from django.urls import include
# Use include() to add paths from the client application
urlpatterns += [
    path('', include('client.urls')),
    #path('', include('employee.urls')),
    path('api/', include('blog.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]