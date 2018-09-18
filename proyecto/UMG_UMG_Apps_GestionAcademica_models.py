from django.db import models

# Create your models here.

class Alumno(models.Model):
    Nombres = models.CharField(max_length=35)
    Apellidos = models.CharField(max_length=35)
    DPI = models.CharField(max_length=10)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS)

    def NombreCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.Nombres, self.Apellidos)

    def __str__(self):
        return self.NombreCompleto()

class Catedratico(models.Model):
    NombreCatedratico=models.CharField(max_length=50)
    TituloAcademico=models.CharField(max_length=50)

    def __str__(self):
        return "{0}({1})".format(self.NombreCatedratico, self.TituloAcademico)

class Curso(models.Model):

    Nombre = models.CharField(max_length=50)
    Creditos=models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)



class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso)
