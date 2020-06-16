# Pyad Library import
from pyad import *

# ADGroup importeren vanuit de pyad library om AD Groups te creeren
from pyad.adgroup import ADGroup

#Padnaam naar de OU gedefineerd via containers.
ou = pyad.adcontainer.ADContainer.from_dn("OU=Gebruikers, OU=Afdeling Servicedesk, OU=Ventishop,DC=ventishop,DC=nl")

#Create security group.
ADGroup.create(name="Uncle Bob", container_object=ou, security_enabled=True, scope='GLOBAL', optional_attributes={})

#Print statement dat het groep is aangemaakt.
print('Group is aangemaakt')

