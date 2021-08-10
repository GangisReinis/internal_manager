from blog.models import attr_blog, attr_tag
from blog.serializers import BlogSerializer
from rest_framework import generics
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html')

class BlogDetail(LoginRequiredMixin, generic.DetailView):
    model = attr_blog

class CreateBlog(LoginRequiredMixin,generic.edit.CreateView):
    model = attr_blog
    fields = [
        "title",
        "post",
        "tag",
        "flag"
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateBlog(LoginRequiredMixin,generic.edit.UpdateView):
    model = attr_blog
    fields = [
        "title",
        "post",
        "tag",
        "flag"
    ]

    template_name_suffix = '_update_form'


class DeleteBlog(LoginRequiredMixin,generic.edit.DeleteView):
    model = attr_blog
    success_url = reverse_lazy('index')
# API views

class BlogListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = attr_blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = attr_blog.objects.all()
    serializer_class = BlogSerializer
