import time
from functools import wraps

def time_exec(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        temps_execution = end - start
        print(f"Temps d'exécution de {f.__name__}: {temps_execution} secondes")
        
        return res

    return wrapper

@time_exec
def foo():
    # Simulation d'une fonction prenant du temps
    time.sleep(2)
    print("Fin de la fonction")

# Utilisation de la fonction décorée
foo()
