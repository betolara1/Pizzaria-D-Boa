from django.db import models
from django.contrib.auth.models import User

class Cardapio(models.Model):
    imagem = models.ImageField(upload_to='imagens_pizzas/')
    
    def __str__(self):
        return self.imagem.name


class Sabores(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome
    

class Preco(models.Model):
    TAMANHO = (
        ('B', 'Broto'),
        ('P', 'Pequena'),
        ('M', 'Média'),
        ('G', 'Grande'),
        ('F', 'Família'),
    )
    tamanho = models.CharField(max_length=1, choices=TAMANHO)
    preco = models.FloatField()

    def __str__(self):
        return self.tamanho
    
    
class Pedidos(models.Model):
    STATUS_PEDIDO = (
        ('1', 'Pendente'),
        ('2', 'Em Preparo'),
        ('3', 'Pronto'),
        ('4', 'Cancelado'),
    )
    TAMANHO = (
        ('B', 'Broto'),
        ('P', 'Pequena'),
        ('M', 'Média'),
        ('G', 'Grande'),
        ('F', 'Família'),
    )
    ENTREGA = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    nome = models.CharField(max_length=50, null=False)
    tamanho = models.CharField(max_length=1, choices=TAMANHO)
    sabores = models.ManyToManyField(Sabores, related_name='sabores')
    observacao = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=STATUS_PEDIDO, null=True)
    preco = models.FloatField(null=True)
    entrega = models.CharField(max_length=1, choices=ENTREGA, null=True)
    
    def __str__(self):
        return self.nome