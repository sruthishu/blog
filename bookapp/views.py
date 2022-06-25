from msilib.schema import ListView
from django.shortcuts import render
from .models import Book
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class home(ListView):
     model= Book
     template_name='base.html'
     fields='__all__'

class BlogDetailview(DetailView):
     model = Book
     template_name='posts.html'
     
class BlogsCreateView(CreateView):
     model = Book
     template_name='new.html'
     fields='__all__'

class BlogUpdateView(UpdateView):
     model = Book
     template_name='post_edit.html'
     fields = ['title','description']
     
class BlogDeleteView(DeleteView):
     model = Book
     template_name = 'post_delete.html'
     success_url =reverse_lazy('home')