from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),  # If 'book_list' is the view you want to use for the home page
    # ... other URL patterns
]
