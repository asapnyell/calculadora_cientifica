import math

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."
def seno(a):
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def raiz_quadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Raiz quadrada de número negativo não é permitida."
def potencia(base, expoente):
    return math.pow(base, expoente)