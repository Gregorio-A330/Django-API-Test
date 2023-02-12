from django.http import JsonResponse
from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Alunos e Alunas""" #docstring

    queryset = Aluno.objects.all() # responsável por trazer os dados do banco de dados (podendo incluir um filtro trazendo por data de nascimento)
    serializer_class = AlunoSerializer #classe responsável por serializar


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos""" #docstring

    queryset = Curso.objects.all() # responsável por trazer os dados do banco de dados (podendo incluir um filtro )
    serializer_class = CursoSerializer #classe responsável por serializar
class MatriculasViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas""" #docstring

    queryset = Matricula.objects.all() # responsável por trazer os dados do banco de dados (podendo incluir um filtro )
    serializer_class = MatriculaSerializer #classe responsável por serializar


# def alunos(request):
#     if request.method == 'GET':
#         aluno = {'id':1, 'nome': 'Gabriel'}
#         return JsonResponse(aluno)
