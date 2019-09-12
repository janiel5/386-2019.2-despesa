from django.contrib import admin
from .models import Despesa


# Register your models here.
class DespesaAdmin(admin.ModelAdmin):
    list_display =  ('data_criacao', 'tipo_despesa', 'descricao', 'forma_pagamento')


admin.site.register(Despesa, DespesaAdmin)
