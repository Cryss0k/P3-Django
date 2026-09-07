from django.urls import path, include
from . import views

app_name = 'inicio'

urlpatterns = [
    # Aquí debes apuntar a la vista que carga tu inicio.html, NO hacer un include
    path('', views.inicio, name='inicio'), 
    
    # Esta línea está correcta, conecta inicio con app1
    path('app1/', include('app1.urls')), 
]