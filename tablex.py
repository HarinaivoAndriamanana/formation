liste1 = [1,2,3,4, 5,6,7,8,["a","b","v"], "Victorien"]

liste2 = liste1[5:]

liste3 = liste1[:5]

print("Liste1 : " , liste1)

print("Liste2 : " , liste2)

print("liste3 : ", liste3)

print(f"Liste1 :  {liste1}")


print("liste1([5:5])", liste1[5:6])

liste1.append("tottop")

print(liste1)

liste1.insert(1,"Tiptip")

print(liste1)

liste1.extend(["hello","code","test"])

print(liste1)

liste1.index()