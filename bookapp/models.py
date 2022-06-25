from django.urls import reverse
from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
     title=models.CharField(max_length=100)
     img=models.ImageField(blank=True)
     description=models.TextField()
     author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
     
     def __str__(self):
          return self.title

     def get_absolute_url(self):
          return reverse('detail_view', args=[str(self.id)])
