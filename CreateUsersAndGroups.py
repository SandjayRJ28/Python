# Pyad Library import
from pyad import *

# ADUser importeren vanuit de pyad library om AD users te creeren
from pyad.adgroup import ADGroup
from pyad.aduser import ADUser

# pandas Library importeren om CSV bestanden uit te lezen
import pandas as pd

ou = pyad.adcontainer.ADContainer.from_dn("OU=Gebruikers, OU=Afdeling Servicedesk, OU=Ventishop,DC=ventishop,DC=nl")
ADGroup.create(name="Uncle Bo", container_object=ou, security_enabled=True, scope='GLOBAL', optional_attributes={})
g = pyad.from_cn("Uncle Bob")

ou = pyad.adcontainer.ADContainer.from_dn("OU=Gebruikers, OU=Afdeling Servicedesk, OU=Ventishop,DC=ventishop,DC=nl")
data = pd.read_csv("usersServicedesk.csv")
wachtwoord = "Password123456!"
names = data["Namen"]

# g.add_members(u)

for i in range(0, len(names)):
    username = names[i]
    new_user = ADUser.create(username, ou, wachtwoord)
    print(username + '\tis aangemaakt!')

    # voeg user toe aan group
    g.add_members(new_user)
