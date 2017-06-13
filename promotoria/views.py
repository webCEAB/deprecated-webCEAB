from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Aspirantes
from .forms import NuevoProspecto
from django.contrib.auth.decorators import permission_required

@permission_required('polls.can_vote')
def promotorianva(request):
	if not request.user.is_authenticated:
		return redirect('index')
	else:
		lista_prospectos_total = Aspirantes.objects.order_by("id")
		return render_to_response('siad/formulario_buscar.html', {'lista_prospectos_total':lista_prospectos_total})

def nuevo_prospecto(request):
	if request.method == 'POST':
		form = NuevoProspecto(request.POST) 
		if form.is_valid():
			form.save()
			print ("Se guardo correctamente")
		print ("No es valido el formulario")
		return redirect('promotorianva')
	else:
		form = NuevoProspecto()
		print ("no se guardaron los datos")
	return render(request, 'siad/nuevo_prospecto.html', {'form': form})

def formulario_buscar(request):
	return render(request, 'siad/formulario_buscar.html')

# Create your views here.
