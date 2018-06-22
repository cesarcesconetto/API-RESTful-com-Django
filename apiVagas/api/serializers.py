from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import *
 

# mapeamento da classe REQUISITO 
class RequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisito
        fields = ["id", "descricao"]
 
# mapeamento da classe VAGA
class VagaSerializer(WritableNestedModelSerializer):
    requisitos_vaga = RequisitoSerializer(many=True)
    class Meta:
        model = Vaga
        fields = ["id", "titulo", "descricao", "salario", "tipo_contrato", "status", "empresa", "requisitos_vaga"]

# mapeamento da classe EMPRESA 
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["id", "nome_fantasia", "cnpj", "email"]