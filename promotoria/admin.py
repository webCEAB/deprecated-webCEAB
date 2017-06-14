from django.contrib import admin
<<<<<<< HEAD
=======
from .models import Aspirantes

class AspirantesAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')
	raw_id_fields = ('Aspirantes',)


admin.site.register(Aspirantes)

>>>>>>> guardar

# Register your models here.
