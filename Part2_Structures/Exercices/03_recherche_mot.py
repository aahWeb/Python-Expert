p = [1,3,7,8,9,1,2,3,8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
w = [1, 2, 3]

def search_word(p, w):
    lenW = len(w)
    lenP = len(p)

    # ici 23 - 3 = 20 , 0 à 20 
    for i in range(lenP - lenW + 1):
        k = 0
        # on avance de la longueur de la séquence que l'on cherche 
        for j in range(lenW):
            # print(p[i + j], end = ' ')
            # on teste si les chiffres sont égaux de manière consécutive, et si on en trouve 3 égaux (ou lenW) c'est que l'on a trouvé la séquence qui est exactement égale à 3 ( ou lenW)
            if p[i + j] == w[j]:
                k += 1 # on compte +1 à chaque fois que l'on en a trouvé 1
        
        if k == lenW:
            return i # l'indice où on a trouvé la séquence

print(search_word(p, w))