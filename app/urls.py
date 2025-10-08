from app.views import pedido
from django.urls import path

urlpatterns = [
    path('pedido/', pedido, name='get_pedido'),
]