from django.contrib import admin
from .models import Plantel, Empleado, ContactoEmpresarial, Empresa, FormaContacto, Documento, Estatus

admin.site.register(Plantel)
admin.site.register(Empleado)
admin.site.register(ContactoEmpresarial)
admin.site.register(Empresa)
admin.site.register(FormaContacto)
admin.site.register(Documento)
admin.site.register(Estatus)