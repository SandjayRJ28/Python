# Pyad Library import
from pyad import *

# ADUser importeren vanuit de pyad library om AD users te creeren
from pyad.aduser import ADUser

# pandas Library importeren om CSV bestanden uit te lezen
import pandas as pd

# Padnaam naar OU gedefineerd
ou = pyad.adcontainer.ADContainer.from_dn("OU=Gebruikers, OU=Afdeling Servicedesk, OU=Ventishop,DC=ventishop,DC=nl")

# Uitlezen van de CSV bestand waarbij we een password toevoegen.
data = pd.read_csv("usersServicedesk.csv")
wachtwoord = "Password123456!"

# Alle namen uit de CSV worden in een List geplaatst
names = data["Namen"]

# Voor elke naam in de CSV bestand wordt de user aangemaakt waar die geplaatst wordt en welke naam en wachtwoord deze heeft.
for i in range(0, len(names)):
    username = names[i]
    print(username + '\tis aangemaakt!')
    new_user = ADUser.create(username, ou, wachtwoord)
