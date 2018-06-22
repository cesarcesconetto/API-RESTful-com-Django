from rest_framework import pagination
 
class PaginacaoVagas(pagination.PageNumberPagination):
    page_size = 2 # serão exibidas apenas 2 vagas por página
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 4
 
class PaginacaoEmpresas(pagination.PageNumberPagination):
    page_size = 3 # serão exibidas apenas 3 empresas por página
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 4