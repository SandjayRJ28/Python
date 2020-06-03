#We hebben vaak datum en tijden nodig wanneer we errors vast willen stellen in een log en de data opslaan
#Om de huidige datum en tijden te krijgen
#Moeten we hiervoor een library gebruiken
from datetime import datetime

huidige_datum = datetime.now()

#De now functie geeft een datetime object terug
print("Vandaag is:" + str(huidige_datum))