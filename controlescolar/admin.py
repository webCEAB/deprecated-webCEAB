from django.contrib import admin
from .models import Estudiante

class AspirantesAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')
	raw_id_fields = ('Estudiante',)


admin.site.register(Estudiante)

# Register your models here.
