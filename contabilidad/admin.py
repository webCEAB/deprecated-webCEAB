from django.contrib import admin
from .models import Proveedor, Pago, Egreso

admin.site.register(Proveedor)
admin.site.register(Pago)
admin.site.register(Egreso)

