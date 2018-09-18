from django.contrib import admin


from UMG.Apps.GestionAcademica.models import*

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Catedratico)
admin.site.register(Curso)
admin.site.register(Matricula)