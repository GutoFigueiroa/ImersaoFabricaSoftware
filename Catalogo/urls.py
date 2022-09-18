from django.urls import path
from .views import home, create, leitura, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'), 
    path('leitura/<int:pk>/', leitura, name='leitura'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
] 