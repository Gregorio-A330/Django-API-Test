from django.http import JsonResponse
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Alunos e Alunas""" #docstring

    queryset = Aluno.objects.all() # responsável por trazer os dados do banco de dados (podendo incluir um filtro trazendo por data de nascimento)
    serializer_class = AlunoSerializer #classe responsável por serializar
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos""" #docstring

    queryset = Curso.objects.all() # responsável por trazer os dados do banco de dados (podendo incluir um filtro )
    serializer_class = CursoSerializer #classe responsável por serializar
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas""" #docstring

    queryset = Matricula.objects.all() # responsável por trazer os dados do banco de dados (podendo incluir um filtro )
    serializer_class = MatriculaSerializer #classe responsável por serializar
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# retorna apenas uma view sem edições
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

# retorna apenas uma view sem edições
class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""

    def get_queryset(self): # passa a instancia pelo self
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# def alunos(request):
#     if request.method == 'GET':
#         aluno = {'id':1, 'nome': 'Gabriel'}
#         return JsonResponse(aluno)
