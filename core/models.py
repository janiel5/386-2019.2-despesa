from django.db import models


# Create your models here.
class Despesa(models.Model):
    data_criacao = models.DateField()
    tipo_despesa = models.CharField(max_length=50)
    descricao  = models.CharField(max_length=250)
    forma_pagamento = {('boleto', 'boleto'),
                       ('credito','credito'),
                       ('debito', 'debito')
                       }
    def __str__(self):
        return str(self.data_criacao)
