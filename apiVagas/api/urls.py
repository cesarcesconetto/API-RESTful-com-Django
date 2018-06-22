from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
 
# Rotas para chamar os métodos
urlpatterns = [
    url(r'^vagas$', VagaList.as_view()),
    url(r'^vagas/(?P<pk>[0-9]+)$', VagaDetalhes.as_view()),
    url(r'^empresas$', EmpresaList.as_view()),
    url(r'^empresas/(?P<pk>[0-9]+)$', EmpresaDetalhes.as_view()),
]