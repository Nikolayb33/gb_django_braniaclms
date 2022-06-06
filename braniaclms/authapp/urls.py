from unicodedata import name
from authapp import views
from django.urls import path, include
from authapp.views import CustomLoginView, RegisterView, CustomLogoutView, EditView
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/', EditView.as_view(), name='edit'),    
]