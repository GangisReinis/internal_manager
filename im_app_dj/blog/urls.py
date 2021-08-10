from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('blog/',views.BlogListView.as_view()),
    path('blog/<int:pk>/',views.BlogDetailView.as_view()),
]