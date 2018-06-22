from django.db import models
 
# Create your models here.
 
TIPO_CONTRATO_CHOICES = (
    ('PJ', 'Pessoa Jurídica'),
    ('CLT', 'Consolidação das Leis do Trabalho')
)

# Atributos da classe/tabela EMPRESA
class Empresa(models.Model):
    nome_fantasia = models.CharField(null=False, max_length=50)
    cnpj = models.CharField(null=False, max_length=20)
    email = models.EmailField(null=False)
 

# Atributos da classe/tabela VAGA
class Vaga(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    descricao = models.TextField(null=False)
    salario = models.FloatField(null=False)
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO_CHOICES, null=False, max_length=50)
    status = models.BooleanField(null=False, default=1)
    empresa = models.ForeignKey(Empresa) #relacionamento com a classe EMPRESA
 
# Atributos da classe/tabela REQUISITO
class Requisito(models.Model):
    descricao = models.TextField(null=False)
    vaga = models.ForeignKey(Vaga, related_name='requisitos_vaga')