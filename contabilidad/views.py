from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Egreso
from .forms import NuevoEgreso

# Create your views here.
def contabilidad(request):
    return render(request,'contabilidad/contabilidad.html')

def nuevo_egreso(request):
	if request.method == 'POST':
		form = NuevoEgreso(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('contabilidad')
	else:
		form = NuevoEgreso()
	return render(request, 'contabilidad/nuevo_egreso.html', {'form': form})

