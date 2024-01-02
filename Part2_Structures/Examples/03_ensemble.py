a =set('aaabbbccc')
print(a)

b = set([1,1,1,2,2, 3])
print(b)

# Opération sur les ensembles

A = {'b', 'a', 'c'}
B = {'r', 'c', 'a'}

# retire les éléments qui existe du premier ensemble avec le deuxième ensemble, lecture de gauche à droite
print( A - B )  # {'b'}

print(B-A) # {'r'}

# union 
A = {'b', 'a', 'c'}
B = {'r', 'c', 'a'}
print(A|B) # {'a', 'b', 'r', 'c'}

# intersection
A = {'b', 'a', 'c'}
B = {'r', 'c'}
print(A&B) # {'c'}

# union exclusive 
A = {'b', 'a', 'c'}
B = {'r', 'c'}
print(A^B) # {'r', 'a', 'b' } 
print(B^A)