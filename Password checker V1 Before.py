#Variablen die ik hier een waarde geef
lenght=0
num=0
sym=0
upper=0
lower=0
numbers="0123456789"
symbols="!@#$%^&*()_+{}:<>?|[]';l,./"
Uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase="abcdefghijklmnopqrstuvwxyz"

print("Voer uw wachtwoord in")

#hier defineer ik dat password user input is
password = input('')

#Tijdelijke variable
leng = len(password)

#Als lengte van de ingevoerde password groter is dan 8 tekens
#veranderd de waarde van lenght naar +1
if leng > 8:
    lenght=lenght+1

#Anders blijft lenght op 0
else:
    print("Voer een wachtwoord in dat 8 tekens zijn of langer")
    lenght=lenght

#For loop gecreerd met tijdelijke variable
#als beide waarde zijn ingevuld/gelijk zijn dan veranderd de waarde van num naar +1
for  a in password:
    for b in numbers:
        if a==b:
            num=num+1

        else:
            num=num

#Hetzelfde loop als voor symbolen
for a in password:
    for c in symbols:
        if a==c:
            sym=sym+1
        else:
            sym=sym

for a in password:
    for d in Uppercase:
        if a==d:
            upper=upper+1
        else:
            upper=upper

for a in password:
    for e in Lowercase:
        if a==e:
            lower=lower+1
        else:
            lower=lower

#Als alle waardes 1 zijn dan betekend dat ze allemaal gebruikt zijn en het Wachtwoord sterk is.
if lenght>= 1 and num>= 1 and sym>= 1 and upper>= 1 and lower>= 1:
    print("Wachtwoord is sterk")

#Anders zegt het script dat het wachtwoord niet sterk genoeg is.
else:
    print("Wachtwoord is niet sterk genoeg")
