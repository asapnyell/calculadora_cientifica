import match

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
    return match.sin(match.radians(a))

def cosseno(a):
    return match.cos(match.radians(a))

def tangente(a):
    return match.tan(match.radians(a))

def raiz_quadrada(a):
    if a >= 0:
        return match.sqrt(a)
    else:
        return "Raiz quadrada de número negativo não é permitida."
def potencia(base, expoente):
    return match.pow(base, expoente)