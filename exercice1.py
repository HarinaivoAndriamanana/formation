liste = []
a = 1
while a <= 100:
    if a % 4 == 0:
        liste.append(a)
    a = a + 1

#print(liste)

liste.sort(reverse = True)
print(liste)

b = []

for i in range(1,100):
    if i % 4 == 0:
        liste.append(b)
    i += 1
print(b)    

#print(liste.count)

liste2 = ["Tana", "Antsirabe"]
for index, ville in enumerate(liste2):
    print(index, ville)
#print(liste)


villes = ["Tana","Antsirabe","Mampikony","Andapa"]
nb_habitants = [15200,1251,5333,8500,800]

for ville, nb in zip(villes, nb_habitants):
    print(ville,nb)


mon_dic = {"Tana": 15200,
           "Antsirabe" : 1251,
           "Mampikony" : 5333,
           "Andapa" : 8500}

print(mon_dic["Andapa"])

mon_dic = {"Tana": [50,10,25,16,15],
           "Antsirabe" : 1251,
           "Mampikony" : 5333,
           "Andapa" : 8500}

print(mon_dic["Tana"][2])

a = [12,34,{"Victorien":12,"pascal":500}, [1,2,3,{"mail" : "harinaivo@login.mg"}]]

print(a[3][3]["mail"])




