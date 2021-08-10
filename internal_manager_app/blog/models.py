from django.db import models
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField

class attr_tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class attr_flag(models.Model):
    name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name

class attr_blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,)
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post = HTMLField(null=True, blank=True,)
    tag  = models.ForeignKey(attr_tag, on_delete=models.DO_NOTHING)
    flag = models.ForeignKey(attr_flag, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']

    def get_absolute_url(self):
        """Returns the url to access a particular client instance."""
        return reverse('blog-detail', kwargs={'pk':int(self.pk)})
