"""
Nous souhaitons créer une fonction qui permet d'inverser des entiers signés ou non :

Par exemples :

-6523 donnerait -3256 

123 donnerait 321
""" 

num = -6523
sign = -1 if num < 0 else 1 # changement de signe
num = sign * num 
num = str(num)

num = sign * int( num[::-1] )

print(num)

def inverse(num):
    sign = -1 if num < 0 else 1 # changement de signe
    num = sign * num 
    num = str(num)

    return sign * int( num[::-1] )

num = -6523
print(inverse(num))
