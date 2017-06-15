from django.contrib import admin
from .models import Plantel, Empleado, ContactoEmpresarial, Empresa

admin.site.register(Plantel)
admin.site.register(Empleado)
admin.site.register(ContactoEmpresarial)
admin.site.register(Empresa)