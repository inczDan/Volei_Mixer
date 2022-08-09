from django.urls import path
from . import views


urlpatterns = [
    path('administracao/', views.create, name='crud.padrao'),
]