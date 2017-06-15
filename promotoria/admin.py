from django.contrib import admin
from .models import Aspirantes

class AspirantesAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')
	raw_id_fields = ('Aspirantes',)

admin.site.register(Aspirantes)