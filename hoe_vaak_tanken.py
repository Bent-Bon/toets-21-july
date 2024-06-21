from math import ceil
import random

def tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand):
    afstand = kilometers_per_liter * tankinhoud
    return ceil(te_rijden_afstand / afstand) - 1

for x in range(10):
    km_l = random.randint(1, 200)
    inhoud = random.randint(1, 10)
    afstand = random.randint(1, 10)
    print(tanken(km_l, inhoud, afstand))

print(tanken(10, 10, 190))