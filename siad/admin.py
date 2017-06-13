from django.contrib import admin
from .models import Alumno, Plantel, Empleado, Servicio, Aspirante, ContactoEmpresarial, Empresa, Pago, Curso, Materia, Proovedor, Egreso

class AlumnoAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')
	raw_id_fields = ('Aspirante',)

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Plantel)
admin.site.register(Empleado)
admin.site.register(Servicio)
admin.site.register(ContactoEmpresarial)
admin.site.register(Empresa)
admin.site.register(Pago)
admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Proovedor)
admin.site.register(Egreso)


