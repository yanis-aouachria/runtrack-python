L = [8, 24, 48, 2, 16]

count = 0  

for num in L:  
    if num % 3 == 0:  # vérifie si le nombre est divisible par 3
        count += 1  

print("Le nombre de multiples de 3 dans la liste est:", count)