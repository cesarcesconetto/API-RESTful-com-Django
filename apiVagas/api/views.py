from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
 
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
 
from .models import *
from .serializers import *
from .pagination import *
 
class VagaList(APIView):
    # Exibir registros
    def get(self, request):
        try:
            lista_vagas = Vaga.objects.all()
            paginator = PaginacaoVagas()
            result_page = paginator.paginate_queryset(lista_vagas, request)
            serializer = VagaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    # Criar novo registro
    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            empresa_id = request.data['empresa']
            Empresa.objects.get(pk=empresa_id)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # se a empresa não existir
        except Empresa.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa a ser relacionada não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
class VagaDetalhes(APIView):
    
    # Exibir registro pelo ID
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga)
            return Response(serializer.data)
        # se a vaga não existir    
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Editar um registro pelo ID
    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga, data=request.data)
            empresa_id = request.data['empresa']
            Empresa.objects.get(pk=empresa_id)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # se a vaga não existir
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        # se a empresa não existir
        except Empresa.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa a ser relacionada não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    # Remover um registro pelo ID
    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            vaga.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # se a vaga não existir
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
class EmpresaList(APIView):

    # Exibir registros
    def get(self, request):
        try:
            lista_empresas = Empresa.objects.all()
            paginator = PaginacaoEmpresas()
            result_page = paginator.paginate_queryset(lista_empresas, request)
            serializer = EmpresaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    # Criar novo registro
    def post(self, request):
        try:
            serializer = EmpresaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # requisição com sucesso
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # requisição sem sucesso
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
class EmpresaDetalhes(APIView):
    
    # Exibir registro pelo ID
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            empresa = Empresa.objects.get(pk=pk)
            serializer = EmpresaSerializer(empresa)
            return Response(serializer.data)
        # se a empresa não existir
        except Empresa.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    # Editar um registro pelo ID
    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            empresa = Empresa.objects.get(pk=pk)
            serializer = EmpresaSerializer(empresa, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # se a empresa não existir
        except Empresa.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    # Remover um registro pelo ID
    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vagas_empresa = Vaga.objects.filter(empresa_id=pk)
            if vagas_empresa:
                return JsonResponse({'message': "A empresa não pode ser excluida pois há vagas relacionadas a ela"},
                                    status=status.HTTP_403_FORBIDDEN)
            empresa = Empresa.objects.get(pk = pk)
            empresa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # se a empresa não existir
        except Empresa.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)