from unicodedata import name
from venv import create
from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDatailView, BlogUpdateView

app_name="blog"

urlpatterns= [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>', BlogDatailView.as_view(), name='detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='detail'),
]