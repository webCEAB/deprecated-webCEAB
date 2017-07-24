from django.contrib import admin
from .models import Estudiante, Materia, Servicio, Curso, Boleta, Documentacion
class EstudianteAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')

	raw_id_fields = ('Aspirante',)
	filter_horizontal = ('materias',) 
	search_fields = ('Aspirante__id',)
class BoletaAdmin(admin.ModelAdmin):
	raw_id_fields = ('alumno',)
	#search_fields = ('alumno__Aspirante__id',)

class DocumentacionAdmin(admin.ModelAdmin):
	raw_id_fields = ('alumno',)
	search_fields = ('alumno__Aspirante__id',)
	filter_horizontal = ('documentacion_entregada',) 
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Materia)
admin.site.register(Servicio)
admin.site.register(Curso)
admin.site.register(Boleta,BoletaAdmin)
admin.site.register(Documentacion,DocumentacionAdmin)