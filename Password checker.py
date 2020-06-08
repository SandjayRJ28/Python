#Het importeren van de library re
import re

#De password variabel heb ik hier een input van een user aan toegewezen om de password in te typen
wachtwoord = input("Voer uw wachtwoord in: ")

#Hier heb ik boolean aan de check variabel toegewezen om checks te draaien
check = True

#Hier heb ik een while loop aangemaakt voor het checken van het wachtwoordt. tot dat niet alle checks klaar zijn zal de boolean ook niet veranderen
while check:
    if (len(wachtwoord) < 8):
        break
    elif not re.search("[a-z]", wachtwoord):
        break
    elif not re.search("[A-Z]", wachtwoord):
        break
    elif not re.search("[0-9]", wachtwoord):
        break
    elif not re.search("[$#@]", wachtwoord):
        break
    else:
        print("Wachtwoord is sterk! ")
        check = False
        break

if check:
    print("Wachtwoord is niet sterk genoeg ")
