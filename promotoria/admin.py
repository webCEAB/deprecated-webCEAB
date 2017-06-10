from django.contrib import admin
from .models import Aspirantes, Estudiante

class AspirantesAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')
	raw_id_fields = ('Aspirantes',)


admin.site.register(Aspirantes)
admin.site.register(Estudiante)

# Register your models here.
