## import tkinter 
from operacoes import *

def calcular(operacao, a, b=None):
    try:

        if operacao == "+":
            return soma(a, b)
        elif operacao == "-":
            return subtrai(a, b)
        elif operacao == "*":
            return multiplica(a, b)
        elif operacao == "/":
            return divide(a, b)
        elif operacao == "sen":
            return seno(a)
        elif operacao == "cos":
            return cosseno(a)
        elif operacao == "tang":
            return tangente(a)
        elif operacao == "√":
            return raiz_quadrada(a)
        elif operacao == "^":
            return potencia(a, b)
        else:
            return "Operação inválida."
        
        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida.")

janela = tkinter.Tk()
janela.title("Calculadora")

tkinter.Label(janela, text="Primeiro Numero:").grid(row=0, column=0)
tkinter.Label(janela, text="Segundo Numero:").grid(row=1, column=0)

entrada_numero1 = tkinter.Entry(janela)
entrada_numero1.grid(row=0, column=1)

entrada_numero2 = tkinter.Entry(janela)
entrada_numero2.grid(row=1, column=1)

label_resultado = tkinter.Label(janela, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2)
