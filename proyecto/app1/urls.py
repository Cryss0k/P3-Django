from django.urls import path
from . import views

app_name = 'app1' # <-- Cambiado de 'inicio' a 'app1'

urlpatterns = [
    path('v1/', views.app1v1, name='app1v1'),
    path('v2/', views.app1v2, name='app1v2'),
]