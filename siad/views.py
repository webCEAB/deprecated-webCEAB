from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from siad.models import Aspirante
from siad.models import Alumno
# Create your views here.
def index(request):
	return render(request, 'siad/index.html', {})

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



from django.shortcuts import render
###############

import numpy as np
def inversion(nCells):
	""" Return the instalation cost of nCells
		
		nCells [int]: The number of cells 
		
		This function returns the cost of instalation of nCells, it takes into consideration that cost do not behaves linearly with the 
		number of cells, the rules to define the cost of instalation are:
		
		1.- Instalation cost: 1-8 cells is $4000.00, 9-16 $8000,00 and so on
		2.- Each cell cost: $7,200.00
		3.- Protection circuit: $5,00.00
		4.- Saler commission: 10%.
		5.- Administration commission: $1,620.00 the very first cell then $720.00 each extra cell
		6.- Utility: 20%
	"""
	if nCells == 0:
		return 0,0,0,0,0,0,0,0
	instCost = 4000*((nCells-1)/8+1)
	cellsCost = 7200*nCells
	protectionCircuitCost = 5000
	partial = instCost + (cellsCost + protectionCircuitCost)
	salerComm = partial*0.1
	admCost = partial*0.1	
	totalCost = partial + salerComm + admCost
	utility = 0.2*partial
	totalCost = partial + salerComm + admCost + utility
	return totalCost,instCost,cellsCost, protectionCircuitCost, partial, salerComm, admCost, utility

def noCeldasRes(consumo):
	""" This function returns the maximum number of needed cells 
		
		consumption [int]: The bimestral consumption of the client
		
		This function returns the maximum number of cells needed to supply the total energy demand based on the bimestral consumption,
	"""
	return consumo/75.0
	
def pagoCFE(consumption):
	""" Computes the charge done to the user according to CFE rates
	    powerDemand [int]: the power used bimonthly by the user
	"""
	basicCost =0.793#0.793 # energy cost according to CFE
	middleCost = 0.956#0.956
	excessCost = 2.802#2.802
	DACcost = 4.370
	iva = 0.16
	powerDemand = consumption
	if powerDemand>500:
 		pagoFijo = 99.84
 		total = pagoFijo + powerDemand*DACcost
 		#return pagoFijo + powerDemand*DACcost
	else:
		if powerDemand>150: # when user is in in middle consumption
			total = 150*basicCost # full first step
			consumption -= 150 # just take into account from  middle to excess step
			if consumption>130: #if consmumption is on the third step
				total+= 130*middleCost
				consumption -= 130
				total += consumption*excessCost
			else:
				total += consumption*middleCost
			#return total
		else:
			total = consumption*basicCost # When user is in basic consumption
			#return total
	return total*(1.0+iva)

def pagoCFEComercial(consumption):
	""" Computes the charge done to the user according to CFE rates, comercial fees
	    powerDemand [int]: the power used bimonthly by the user
	"""
	basicCost = 2.780
	middleCost = 3.356
	excessCost = 3.699
	iva = 0.16
	pagoFijo =  	65.93
	#	print("El consumo recibido es: ",consumption)
	#print("El consumo recibido es:",consumption)
	total = pagoFijo + consumption*basicCost # When user is in basic consumption
 	if consumption>100: # when user is in in middle consumption
		total = pagoFijo+100*basicCost # full first step
		consumption -= 100 # just take into account from  middle to excess step
		if consumption>100: #if consmumption is on the third step
			total+= 100*middleCost
			consumption -= 100
			if consumption>0:
				total+= consumption*excessCost
		else:
			total += consumption*middleCost
	#print(consumption,total)
	return total*(1.0+iva)

###############
# Create your views here.
def index(request):
	return render(request, 'siad/index.html', {})

def atributos_meta(request): 
	valor = request.META.items() 
	valor.sort() 
	html = [] 
	for k, v in valor: 
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v)) 
	return HttpResponse('<table>%s</table>' % '\n'.join(html)) 
def residencial(request,consumo):
	#instance = Post.objects.get(id=3) # this is the wrong way, do no do this
	#instance = get_object_or_404(Post,id=id)
	consumo = int(consumo)
	pagoActual = pagoCFE(consumo)
	pagoAnterior = pagoActual
	#print "nCell\tpagoCFE \tInvers\tAhorro\tROI"
	nCells = 0 
	datos = []
	while consumo>0:
		ahorro = pagoActual-pagoCFE(consumo)
		inver = inversion(nCells)[0]
		pago = pagoCFE(consumo)
		if ahorro != 0:
			datos.append([str(nCells),str(round(pago,2)),str(round(inver,2)),str(round(ahorro,2)),str(round((inver/ahorro)/6.0,2)),str(round(pagoAnterior-pago,2))])
		else:
			datos.append([str(nCells),str(round(pago,2)),str(round(inver,2)),str(round(ahorro,2)),"No hay retorno de inversion" ,str(round(pagoAnterior-pago,2))])
		pagoAnterior = pago
		nCells += 1
		consumo -= 75
	
	context = {
				"title":"Cotizacion residencial",
			    "datos":datos}
	return render(request,"residencial.html",context)

def comercial(request,consumo):
	#instance = Post.objects.get(id=3) # this is the wrong way, do no do this
	#instance = get_object_or_404(Post,id=id)
	consumo = int(consumo)
	pagoActual = pagoCFEComercial(consumo)
	pagoAnterior = pagoActual
	#print "nCell\tpagoCFE \tInvers\tAhorro\tROI"
	nCells = 0 
	datos = []
	while consumo>0:
		ahorro = round(pagoActual-pagoCFEComercial(consumo),2)
		inver = round(inversion(nCells)[0],2)
		pago = round(pagoCFEComercial(consumo),2)
		if ahorro != 0:datos.append([str(nCells),str(round(pago,2)),str(round(inver,2)),str(round(ahorro,2)),str(round((inver/ahorro)/6.0,2)),str(round(pagoAnterior-pago,2))])
		else:
			datos.append([str(nCells),str(round(pago,2)),str(round(inver,2)),str(round(ahorro,2)),"No hay retorno de inversion" ,str(round(pagoAnterior-pago,2))])
		pagoAnterior = pago
		nCells += 1
		consumo -= 75
	
	context = {
				"title":"Cotizacion Comercial",
			    "datos":datos}
	return render(request,"residencial.html",context)
def instrucciones(request):
	return HttpResponse("En la barra de direcciones debes de agregar residencial o comercial seguido de la diagonal / y despues el consumo, por ejemplo /residencial/510 te arroja la cotizacion para residencial con un consumo de 510 kwh")

def docIncompleta(request):
	
	datos = Alumno.objects.filter(documentacionCompleta=True)
	
	
	context = {
				"title":"Alumnos con documentacion incompleta",
			    "datos":datos}
	return render(request,"residencial.html",context)