from pyad import aduser

import pandas as pd

#Namen die in het CSV bestand staan worden geimporteerd.
data = pd.read_csv("user.csv")
names = data["Namen"]


#For Loop voor elke naam uit het CSV bestand wordt bekeken
for i in range(0, len(names)):
    username = names[i]
    user = aduser.ADUser.from_cn(username)
    user_atrri = user.get_user_account_control_settings()
    print(username + '\tAccount Disabled?\t' + str(user_atrri['ACCOUNTDISABLE']))
    print(username + '\tPassword Expired?\t' + str(user_atrri['PASSWORD_EXPIRED']))
    print(username + '\tAccount Lockout?\t' + str(user_atrri['LOCKOUT']))