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

consumo = 800
pagoActual = pagoCFE(consumo)
pagoAnterior = pagoActual
print "nCell\tpagoCFE \tInvers\tAhorro\tROI"
nCells = 0 
while consumo>0:
	ahorro = pagoActual-pagoCFE(consumo)
	inver = inversion(nCells)[0]
	pago = pagoCFE(consumo)
	if ahorro != 0:
		print nCells,"\t",pago,"\t",inver,"\t",ahorro,"\t",(inver/ahorro)/6.0,"\t",pagoAnterior-pago
	else:
		print nCells,"\t",pago,"\t",inver,"\t",ahorro,"\t","no hay retorno de inversion","\t",pagoAnterior-pago
	pagoAnterior = pago
	nCells += 1
	consumo -= 75
