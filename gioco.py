#!/usr/bin/ python
# -*- coding: utf-8 -*-
print "Benvenuto! Il tuo obiettivo, ben poco nobile, è di evitare che la gente si vaccino. Perché? Da quando i fenici hanno inventato il danaro, la risposta è quella ;) \n Ovviamente, qui giochiamo con vite finte, numeri in variabili, non con vite vere."
print "Gioco sviluppato da Sciking"
vaccinati = 960
popolazione = 1000
nonvaccinati = 40
adepti = 100
konrad = 0
soldi = 10000
morti = 0
turno = 0
import os, random
def poss():
	os.system('cls' if os.name == 'nt' else 'clear')
	global adepti
	global soldi
	global morti
	global konrad
	global vaccinati, popolazione, nonvaccinati, turno
	konrad = random.randint(1,5) 
	if turno%2 == 0:
		if konrad == 1:
			print "Perdi una causa in appello, e paghi 15000€ di spese"
			soldi = soldi - 15000
			adepti = adepti + random.randint(-20,10)
			
		elif konrad == 2:
			print "Ottieni 5000€ di sovvenzione da un'azienda di medicina alternativa"
			soldi = soldi + 5000
		elif konrad == 3:
			print "Vai in Africa. E ti vaccini contro l'epatite. Epic fail"	#l'è ver!
			adepti = adepti - random.randint(10,50)
			soldi = soldi - 25 #e dai 25€ ai quei malvagioni di big pharma svelia!!11!!!  :D
		elif konrad == 4:
			print "La trasmissione 'Ridens' ti dà corda e condivide le tue cagate."
			adepti = adepti + 10
			nonvaccinati = nonvaccinati - 8
			vaccinati = vaccinati + 8
		elif konrad == 5:
			print "Il ministro della Salute attua misure molto restrittive contro i non vaccinati"
			vaccinati = vaccinati + 15
			nonvaccinati = nonvaccinati - 15
	else:
		if konrad == 1:
			print "Riesci a diffondere la notizia che i vaccini causano autismo, con uno studio falso"
			adepti = adepti + 20
			nonvaccinati = nonvaccinati + 10
			vaccinati = vaccinati - 10
		elif konrad == 2:
			print "Un focolaio di morbillo causato dalle tue stronzate, pardon, opinioni dell'altra campana \n causa 3 morti. E vieni denunziato per epidemia colposa"
			morti = morti + 3
			soldi = soldi - 5000
			nonvaccinati = nonvaccinati - 10
			vaccinati = vaccinati + 10
			
		elif konrad == 3:
			print "Vieni pagato 2500€ per diffondere cure naturali ai danni da vaccino"
			soldi = soldi + 2500
		elif konrad == 4:
			print "Ti respingono in frontiera mentre volevi andare all'estero perché socialmente pericoloso"
			adepti = adepti - 25
		elif konrad == 5:
			print "Sfidi i medici a chi dimostra l'esistenza del morbillo. Lo dimostrano e devi pagare 10000€"
			soldi = soldi - 10000
	gioco()
def gioco():
	global adepti
	global soldi
	global vaccinati, popolazione, nonvaccinati, turno, morti
	turno = turno + 1
	soldi = soldi + (adepti*0.5)
	soldi = int(soldi)
	soldi = soldi - 250
	if vaccinati > 1000:
		vaccinati = 1000
		nonvaccinati = 0
	if adepti < 0:
		adepti = 0
	print "*"*10
	if morti > 300:
		print "Un magistrato si sveglia e ti manda in galera per omicidio e epidemia colposa. Pace amen"
		essit()
	if vaccinati < 800:
		print "Immunità di gregge danneggiata \n"
		morti = morti + random.rantint(1,25)
	print turno, "° turno"
	print "Possiedi ", soldi, "Euro"
	print "Hai", adepti, "adepti"
	print "Percentuale Vaccinati: ", vaccinati/10
	print "Morti a causa tua:", morti
	if soldi < 0:
		print "Sei senza soldi"
		essit()
		
	print"""
Menù di gioco \n
1) Studio scientifico falso \n
2) Finanzia false cure \n
3) Cause per danni da vaccino \n
4) Finanzia blog fuffari \n
5) Minaccia di denunzia i debunker \n
6) Campagna pubblicitaria
"""
	kappa = input(">>")
	if kappa == 1:
		print "Vuoi spendere 15000 € per finanziare uno studio sui danni da vaccino, ovviamente falsi?"
		ll = raw_input("Si per accettare: ")
		if ll == "Si":
			soldi = soldi - 15000
			adepti = adepti + 50
		if random.randint(1,10) > 6:
			nonvaccinati = nonvaccinati + 5
			vaccinati = vaccinati - 5

	elif kappa == 2:
		print "Vuoi spendere 10000€ per finanziare un naturopata per curare i danni da vaccino?"
		ll = raw_input("Si per accettare: ")
		if ll == "Si":
			soldi = soldi - 10000
			adepti = adepti + 25
	elif kappa == 3:
		if random.randint(1,10):
			print "Hai vinto la causa: La famiglia verrà risarcita con 100000€ e tu ne prenderai il 10%"
			soldi = soldi + 10000
		else:
			print "Perdi la causa e spendi 10000€ di spese legali"
			soldi = soldi - 10000
	elif kappa == 4:
		print "Dai 1000€ a dei blog fuffari"
		soldi = soldi - 1000
		adepti = adepti + 25
	elif kappa == 5:
		print "Minacci di denuncia i debunker"
		adepti = adepti + random.randint(-5,5)
		ukulele = random.randint(-15,15)
		vaccinati = vaccinati + ukulele
		nonvaccinati = nonvaccinati - ukulele
	elif kappa == 6:
		print """Che campagna vuoi avviare?
1) Rivista (1000€)
2) Trasmissione TV (2000€)
3) Blog fuffaro (5000€)
4) Famiglia finta (10000€)
5) Esci
"""
		camp = input(">")
		if camp == 1:
			adepti = adepti + 30
			soldi = soldi - 1000
		elif camp == 2:
			adepti = adepti + 40
			nonvaccinati = nonvaccinati + 2
			vaccinati = vaccinati - 2
			soldi = soldi - 2000
		elif camp == 3:
			adepti = adepti + 50
			nonvaccinati = nonvaccinati + 4
			vaccinati = vaccinati - 4
			soldi = soldi - 5000
		elif camp == 4:
			adepti = adepti + 50
			nonvaccinati = nonvaccinati + 5
			vaccinati = vaccinati - 5
			soldi = soldi - 10000
			
			

	raw_input("Premi invio per continuare")
		
		
	poss()	
def essit():
	print "Il gioco è finito. Spero ti sia  piaciuto."
	exit()
gioco()
