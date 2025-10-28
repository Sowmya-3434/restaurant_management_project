from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
    path('menu-categories/', views.MenuCategoryListView.as_view(), name='menu-categories'),
    
]