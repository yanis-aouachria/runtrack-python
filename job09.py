#listse
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# calcul du minimum
minimum = L[0]  
for element in L:
    if element < minimum:
        minimum = element

# calcul du maximum
maximum = L[0]  
for element in L:
    if element > maximum:
        maximum = element

# affichage des résultats
print("Minimum:", minimum)
print("Maximum:", maximum)