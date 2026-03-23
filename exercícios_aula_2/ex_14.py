import math

def diagonal(b, h):
    diagonal_qu = b ** 2 + h ** 2
    diagonal = math.sqrt(diagonal_qu)
    return diagonal

print(diagonal(3, 4))