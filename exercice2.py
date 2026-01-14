# Version corrigée
mon_dict = {"nombre_premier": [], "autres": []}

for i in range(2, 12000):
    est_premier = True
    for j in range(2, i):
        if i % j == 0:
            est_premier = False
            break
    
    if est_premier:
        mon_dict["nombre_premier"].append(i) 
    else:
        mon_dict["autres"].append(i)

print("Nombres premiers:", mon_dict["nombre_premier"])
print("Autres nombres:", mon_dict["autres"])
