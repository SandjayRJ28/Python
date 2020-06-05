#Types errors die je kan tegenkomen hieronder een enkele voorbeelden
##Syntx error als je iets vergeet zoals brackets bij een if statement
#x = 12
#y = 34
#if  x == y
#print("success!!")

#runtime error is 99% altijd in je code
#a = 23
#b = 0
#print(a / b)

#print statements plaatsen tussen je code om te zien welke code een error geeft.
#try:
#    print(a / b)
#    except ZeroDivisionError as e:
#           print("raar er gaat iets verkeerd")
#        except:
#            print("Jammer er gaat nu echt iets verkeerd")
#        finally:
#            print("Dit draait altijd of success of verkeerd")
                                 
#logic errors
#x = 202
#y = 23
#if x < y:
#    print(str(x) + "Is groter dan " + str(y))

x = 34
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print("Je mag niet delen door 0")
else:
    print("Er ging iets anders verkeerd")
finally:
    print("Dit is een opschonings code")