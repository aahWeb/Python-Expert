
import functools
                      
def memoize(a_decorer):
    # on décore la fonction pour qu'elle ait les
    # propriétés de a_decorer : __doc__ et __name__
    @functools.wraps(a_decorer)                  
    def decorator (*args):
        try:
            res = decorator.cache[args]
            
            return res
        except KeyError:
            print(args, "keyErrors")
            # on fait vraiment le calcul
            res = a_decorer(*args)
            # on le range dans le cache
            decorator.cache[args] = res
            # on le retourne
            return res
    # on initialise l'attribut 'cache'
    decorator.cache = {}
    return decorator

@memoize
def factoriel(n: int )-> int:
    
    return n if n <= 1 else factoriel( n-1 ) * n 
