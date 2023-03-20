message= "je suis un crack du developemet"


def decale_cesar(message, decalage):
    message_decale = ""
    for lettre in message:
        if lettre.isalpha():
            # calculer l'indice de la lettre après décalage
            indice = ord(lettre) + decalage
            # gérer le dépassement de l'alphabet
            if lettre.islower():
                if indice > ord('z'):
                    indice = ord('a') + (indice - ord('z') - 1)
                elif indice < ord('a'):
                    indice = ord('z') - (ord('a') - indice - 1)
            elif lettre.isupper():
                if indice > ord('Z'):
                    indice = ord('A') + (indice - ord('Z') - 1)
                elif indice < ord('A'):
                    indice = ord('Z') - (ord('A') - indice - 1)
            # ajouter la lettre décalée au message décalé
            message_decale += chr(indice)
        else:
            message_decale += lettre
    print(message_decale)
decale_cesar(message,3)


decale_cesar(decale_cesar(message,3),-3)





     