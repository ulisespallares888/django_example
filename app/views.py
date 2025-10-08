from django.shortcuts import render
from .models import Usuario, Producto, Pedido
from django.http import JsonResponse

# Create your views here.

def pedido(request):
    pedidos = list(Pedido.objects.values())
    # hateoas links could be added here if needed
    pedidos_with_links = []
    for pedido in pedidos:
        pedido['links'] = {
            'self': f"/pedido/{pedido['id']}/",
            'usuario': f"/usuario/{pedido['usuario_id']}/"
        }
        pedidos_with_links.append(pedido)
    return JsonResponse(pedidos, safe=False)