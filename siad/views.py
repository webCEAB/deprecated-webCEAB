from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render
from django.core.mail import send_mail

from siad.models import Aspirante
# Create your views here.
def post_list(request):
	return render(request, 'siad/post_list.html', {})

def fecha_actual(request):
	ahora = datetime.datetime.now()
	#t = get_template('fechaActual.html')
	#html = t.render(Context({'fecha_actual':ahora}))
	#return HttpResponse(html)
	return render(request,'siad/fechaActual.html',{'fecha_actual':ahora})
def horas_adelante(request, horas):
	try:
		horas = int(horas)
	except ValueError:
		raise Http404()
	tiempo = datetime.datetime.now()+datetime.timedelta(hours=horas)
	return render(request,'horas_adelante.html',{'hora_siguiente':tiempo,'horas':horas})
def atributos_meta(request): 
	valor = request.META.items() 
	valor.sort() 
	html = [] 
	for k, v in valor: 
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v)) 
	return HttpResponse('<table>%s</table>' % '\n'.join(html)) 
def formulario_buscar(request):
	return render(request, 'formulario_buscar.html')
def buscar(request): 
	error = False 
	if 'q' in request.GET: 
		q = request.GET['q'] 
		if not q: 
			error = True 
		else: 
			libros = Aspirante.objects.filter(nombre__icontains=q) 
			return render(request, 'resultados.html', {'aspirantes': libros, 'query': q}) 
 
	return render(request, 'formulario_buscar.html', {'error': error}) 
def contactos(request): 
    if request.method == 'POST': 
        form = FormularioContactos(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            send_mail( 
                cd['asunto'], 
                cd['mensaje'], 
                cd.get('email', 'noreply@example.com'), 
                    ['siteowner@example.com'], 
             ) 
            return HttpResponseRedirect('/contactos/gracias/') 
    else: 
        form = FormularioContactos() 
    return render(request, 'formmulario_contactos.html', {'form': form}) 	