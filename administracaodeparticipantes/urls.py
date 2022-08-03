from django.urls import path
from . import views

urlpatterns = [
    path('administracao/', views.crud, name='crud.padrao'),
]