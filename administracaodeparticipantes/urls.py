from django.urls import path
from .views import Crud


urlpatterns = [
    path('administracao/', Crud.as_view(), name='crud.padrao'),
]