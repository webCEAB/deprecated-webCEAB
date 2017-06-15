from django.contrib import admin
<<<<<<< HEAD

from .models import Aspirantes, Estudiante
=======
from .models import Aspirantes
>>>>>>> 89b6ba607cb306d585a2d3e5d39498dc16807940

class AspirantesAdmin(admin.ModelAdmin):
#	list_filter = ('plantelRegistro')
	raw_id_fields = ('Aspirantes',)


<<<<<<< HEAD
admin.site.register(Aspirantes)
admin.site.register(Estudiante)


# Register your models here.
=======
admin.site.register(Aspirantes)
>>>>>>> 89b6ba607cb306d585a2d3e5d39498dc16807940
