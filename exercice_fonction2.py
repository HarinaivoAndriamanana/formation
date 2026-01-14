import math

def second_degree(a, b, c) :
    delta = b**2 - 4*a*c
    if delta > 0 :
        #print("Deux solutions")
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return ["Deux solution", x1, x2]
    elif delta == 0 :
        #print("Solution unique")
        x1 = (-1)*int(b)/(2*int(a))
        return ["Solution unique, x1"]
    else :
        #print("Delta négatif, pas de solution")
        return ["Pas de solution"]


solution = second_degree(1,9,1)

print(solution)
