'''
Docstring for exercice_fonction
f(x) = ax² + bx -c

'''
import math

a = input("Donner une valeur de a : ")
b = input("Donner une valeur de b : ")
c = input("Donner une valeur de c : " )

delta = int(b)*int(b) - (4*int(a)*int(c))

if delta < 0 :
    print("Pas de solution")
elif delta == 0 :
    print("Solution unique", (-1)*int(b)/(2*int(a)))
else :
    print("Solution :" , ((-1) + math.sqrt(delta))/2*int(a))
