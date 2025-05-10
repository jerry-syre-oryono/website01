from django.urls import path
from . import views           # Import views from the current directory

urlpatterns = [
    path('', views.posts_list),  # Changed to empty string since posts/ is handled by the main urls.py
]