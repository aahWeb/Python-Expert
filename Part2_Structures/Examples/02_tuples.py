

t = 'a', 'b', 'c'

print(t)

print( t[0] )

# on peut changer les valeurs d'un tuple
try:
    t[0] = 1
except TypeError:
    print("attention impossible d'assigner une valeur à un tuple")
# on peut redéfinir avec la même variable  
t = 'a', 'b', 'c', 'd'

print(t)

# tuple de tuple
t = 'a', 'b', 'c'

u = t, (1,2,4)
print(u)

t = ('a', 'b', 'c')
# unpackting 
x,y,z = t
print(x, y, z) # variables qui capturent les valeurs du tuple par unpacking

# liste de tuples avec la fonction zip
languages = ['JS', 'Python', 'PHP'] 
versions = [6, 3, 8] 
# une liste de tuple
print(list(zip(languages,versions )))
for u, v in zip(languages,versions ):
    print(f"u :{u}, v: {v}")

x, *y = ( 100, (200, 300 ), (500, 900) )   
print(x)
print(y) # capture le reste dans une liste opérateur étoile 