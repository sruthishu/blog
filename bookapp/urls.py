from unicodedata import name 
from django.urls import *
from .views import *
from .import views
urlpatterns =[
     path('',home.as_view(),name='home'),
     path('post/new',BlogsCreateView.as_view(),name='new_post'),    
     path('post/<int:pk>/',BlogDetailview.as_view(),name='detail_view'),
     path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name='post_edit'),
     path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
]