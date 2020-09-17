from random import random
def is_in():
    a = random() # choisit un nombre aléatoire entre 0 et 1
    b = random()
    x = -1 + 2 * a # absisse d'un point M comprise entre -1 et 1
    y = -1 + 2 * b # ordonnée de M comprise entre -1 et 1
    
    d = ( x**2 + y**2 )**0.5 # distance OM
    if d <= 1: # si M est dans le disque...
        return 1
    else:     # sinon...
        return 0

N = 0 # nombre de points à l'intérieur du disque
f = 10000
for n in range(f):
    N += is_in()
print("PI est à peu près égal à {}".format(4 * N / f))