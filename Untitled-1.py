import random
target_number = random.randint(1, 100)
print(target_number)
valiny = False
tentative = 1
print("Vous avez 8 tentatives")
print("Tentative : ", tentative)
nombre = input("Donner votre nombre : ")
while valiny == False and tentative <= 8:
    if int(nombre) == target_number:
        print("Félicitation")
        valiny = True
        break
    elif int(nombre) < target_number:
        print("Un peu plus")
        valiny = False
    elif int(nombre) > target_number:
        print("Un peu moins")
        valiny = False
    valiny = False
    tentative += 1
    print("Tentative : ", tentative, "Il vous reste " , str(8-tentative))
    nombre = input("Donner votre nombre : ")
    