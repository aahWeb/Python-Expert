# Introduction 

## Présentation 

C'est une fonction ou classe Python modifiant le comportement d'une autre fonction Python.

Une fonction Python est un objet, et un objet peut être assigné à une variable.

On les utilises :

- Journalisation (Logging) 
- Chronométrage
- Validation des arguments
- Gestion d'autorisations 
- Cache de résultats ( voir l'exercice à détailler plus loin )
- Traitement des exceptions
- Transformation de fonctions
- Méta-programmation

## Décorateur avec une fonction

Découvrons les décorateurs avec quelques exemples.

- **Exemple 1** trace décore une fonction sans paramètre.

Dans l'exemple suivant on a la construction d'un décorateur sans l'opérateur @.

```python
def trace(func):
    def decorateur():
        print("Début d'appel à", func)
        func()
        print("Fin d'appel à", func)
    return decorateur

# Manière simple de décorer la fonction do_something
def do_something():
    print("doing something")

do_something = trace(do_something)
do_something()
```

**Mais on peut faire la même chose avec le pie opérateur.**

```python

@trace
def do_something():
    print("doing something")

do_something()
```

- **Exemple 2** Décorateurs avec fonction ayant des paramètres

```python
def trace(func):
    def decorator(*args, **kwargs):
        print("Début d'appel à", func.__name__)
        res = func(*args, **kwargs)
        print("Fin d'appel à", func.__name__)

        return res

    return decorator

@trace
def average(*args):
    """Calcule la moyenne d'une série de nombre(s)."""
    nb = len(args)
    s = 0
    for y in args:
        s += y

    return round( s / nb, 2 )

print( average(5, 2, 2) )
```

Si on fait un help(average), on aura l'affichage suivant :

```txt
Help on function decorator in module __main__:
decorator(*args, **kwargs)
```

En effet, la méthode average a été décorée. C'est donc la documentation de la méthode interne decorator(*args, **kwargs) qui s'affiche et nous avons perdu la véritable documentation d'origine de la fonction average.

On corrigera ce problème en utilisant le décorateur @wraps du module functools

```python
from functools import wraps

def trace(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print("Début d'appel à", func.__name__)
        res = func(*args, **kwargs)
        print("Fin d'appel à", func.__name__)

        return res

    return decorator

# on redécore la fonction 
@trace
def average(*args):
    """Calcule la moyenne d'une série de nombre(s)."""
    nb = len(args)
    s = 0
    for y in args:
        s += y

    return round( s / nb, 2 )

print( average(5, 2, 2) )

# si on demande la documentation de la fonction elle correspondra.
help(average)
```

- **Exemple 3** décorateur avec paramètre(s)

```python
def decorator_params(a, b):
    def decorator(func):

        def wrapper_decorator(*args, **kwargs):
            c, d = args
            print(f"Paramètre du décorateur : {a, b} - param de la fonction decorée {c, d}")
            res = func(*args, **kwargs)

            return res

        return wrapper_decorator

    return decorator

# Appels de fonction avec décoration paramétriques

@decorator_params( a=1, b = 3)
def do(c, d):
    print("Fonction exécutée")

do(1, 2)

# On peut bien sûr appeler le décorateur avec paramètres
@decorator_params(5, 6)
def do(c, d):
    print("Fonction exécutée")

do(1, 2)
```

## 01 Exercice calculer le temps d'exécution

En utilisant le module **time**, créez un décorateur qui permet de calculer le temps d'exécution d'une fonction. Voyez une utilisation ci-dessous :

```python
import time

# Définissez votre décorateur timer ici 

@timer
def my_fun():
    pass
```

## 02 Exercice factorielle 

Créez un décorateur **memorize**, il permet de mettre, dans un système de cache, le résultat précédent de la fonction factoriel, factoriel est implémentée de manière récursive, voyez le code ci-dessous pour cette fonction.

```python
import typing 

# TODO @memorize

@memorize
def factoriel(n: int )-> int:
    
    return n if n <= 1 else factoriel( n-1 ) * n 
```

## Définition d'un décorateur avec une classe

On peut uiliser une classe pour définir un décorateur :

```python

class A:
    def __init__(self, f):
        self.count = 0
        self.f = f

    def __call__(self, *t, **d):
        self.count += 1
        print( f"{self.f.__name__} : {self.count}" )

        return self.f(*t, **d)

@A
def f(a, b):
    print(a, b)

f(1, 2)
```

## 03 Exercice factorielle 

Créez un décorateur avec une classe cette fois **Memorize**, il permet de mettre, dans un système de cache, le résultat précédent de la fonction factoriel, factoriel est implémentée de manière non récursive, voyez le code ci-dessous pour cette fonction.

```python
import typing

def factoriel(n: int , end: int = 0)-> int:
    res = 1
    while n > end:
        res *= n
        n = n - 1
    
    return res
```

## Classe décorateur avec paramètres

Le principe est le même que pour les fonctions qui définisse un décorateur avec paramètres, le wrapper est dans la méthode dunder call.

```python
import typing

class A:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            print(f"Paramètre du décorateur de classe : {self.p , self.q}")
            res = f(*args, **kwargs)

            return res

        return wrapper

# Utilisation du décorateur de classe avec paramètre
@A(q=1, p=3)
def do_something():
    print("Fonction exécutée")

# Appel de la fonction décorée
do_something()
```
