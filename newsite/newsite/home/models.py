from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Entries(models.Model):
    title = models.CharField(max_length=50)
    # body = RichTextField(blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.title + '|' + str(self.author)


    def get_absolute_url(self):
        return reverse('home')
    