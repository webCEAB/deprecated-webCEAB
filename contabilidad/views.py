from django.shortcuts import render

# Create your views here.
def contabilidad(request):
    return render(request,'contabilidad/contabilidad.html')