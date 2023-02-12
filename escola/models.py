from django.db import models

# Create your models here.
#  Após criar os modelos é necessário migrar pro banco de dados
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    # declaração de constante
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
            ('M', 'Matutino'),
            ('V', 'Verpertino'),
            ('N', 'Noturno')
    )

    # Eu ja tenho este aluno criado em outra tabela eu só quero o ID e armazenar nesta matricula
    # primeiro parametro da foreignKey é qual tabela vou utilizar, quem vai ser responsável por mandar essa primaryKey
    #segundo parametro é para caso o ALUNO FOR DELETADO ele também vai remover as matriculas associadas ao ID
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
