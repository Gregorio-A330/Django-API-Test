from django.contrib import admin
from escola.models import Aluno, Curso
# Register your models here.

# configurações para exibição
class Alunos(admin.ModelAdmin):
        list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento') # listagem dos campos no admin - estilo swagger
        list_display_links = ('id', 'nome') # campos que podem ser editados
        search_fields = ('nome',) # consegue realizar a busca por nome
        list_per_page = 20 # paginação

# passando duas informações (modelo e qual a configuração )
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
        list_display = ('id', 'codigo_curso', 'descricao',) # listagem dos campos no admin - estilo swagger
        list_display_links = ('id', 'codigo_curso') # campos que podem ser editados
        search_fields = ('codigo_curso',) # consegue realizar a busca por nome

admin.site.register(Curso, Cursos)

# python manage.py runserver
# localhost:8000/admin