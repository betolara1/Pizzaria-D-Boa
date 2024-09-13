from django.urls import path
from . import views
    

urlpatterns = [
    path('cardapio/', views.cardapio, name='cardapio'),
    path('pedido/', views.pedido, name='pedido'),
    path('fecharpedido/', views.fecharpedido, name='fecharpedido'),
    path('meuspedidos/', views.meuspedidos, name='meuspedidos'),
    path('excluirpedido/<int:pedido_id>', views.excluirpedido, name='excluirpedido'),
]