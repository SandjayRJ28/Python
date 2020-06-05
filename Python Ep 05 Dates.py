#We hebben vaak datum en tijden nodig wanneer we errors vast willen stellen in een log en de data opslaan
#Om de huidige datum en tijden te krijgen
#Moeten we hiervoor een library gebruiken
from datetime import datetime, timedelta

huidige_datum = datetime.now()

#De now functie geeft een datetime object terug
print("Vandaag is:" + str(huidige_datum))

#De functie timedelta wordt gebruikt voor het defineren van een periode.
een_dag = timedelta(days=1)
gisteren = huidige_datum - een_dag
print("Gisteren was: " + str(gisteren))

#Gebruik date functies on je datum controle te geven over fortmatting
print("Dag: " + str(huidige_datum.day))
print("Maand: " + str(huidige_datum.month))
print("Jaar: " + str(huidige_datum.year))

#Soms krijg je datum als een string maar moet je het converten naar een datetime object
verjaardag = input("Wanneer je ben je jarig (dd/mm/yyyy)? ")
verjaardag_datum = datetime.strptime(verjaardag, "%d/%m/%Y")
print("Verjaardag " + str(verjaardag_datum))
een_dag1 = timedelta(days=1)
verjaardag_gisteren = verjaardag_datum - een_dag1
print("Dag voor je verjaardag: " + str(verjaardag_gisteren))