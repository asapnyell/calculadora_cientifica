import tkinter as tkinter
import tkinter as tk
from operacoes import *

def calcular():
    operacao = operacao_selecionada.get()
    try:
        a = float(entrada_numero1.get())
        if operacao in["+", "-", "*", "/", "^"]:
            segundo_numero = entrada_numero2.get().strip()
            if segundo_numero == "":
                label_resultado.config(text="Erro: Segundo número é necessário para esta operação.")
                return
            b = float(segundo_numero)
        else:
            b = None

        if operacao == "+":
            resultado= soma(a, b)
        elif operacao == "-":
            resultado= subtrai(a, b)
        elif operacao == "*":
            resultado= multiplica(a, b)
        elif operacao == "/":
            resultado= divide(a, b)
        elif operacao == "sen":
            resultado= seno(a)
        elif operacao == "cos":
            resultado= cosseno(a)
        elif operacao == "tang":
            resultado= tangente(a)
        elif operacao == "√":
            resultado= raiz_quadrada(a)
        elif operacao == "^":
            resultado= potencia(a, b)
        else:
            resultado= "Operação inválida."

        label_resultado.config(text=f"Resultado: {int(resultado)}")

    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida.")
        return
def atualizar_campos(*args):
    op = operacao_selecionada.get()
    if op in ["+", "-", "*", "/", "^"]:
        entrada_numero2.config(state="normal")
    else:
        entrada_numero2.delete(0, tk.END)
        entrada_numero2.config(state="disabled")    

## Interface Gráfica
janela = tk.Tk()
janela.title("Calculadora Inteligente")
janela.geometry("400x300")
janela.resizable(False, False)
# Variável para armazenar a operação selecionada

tk.Label(janela, text="Primeiro Numero:").pack(pady=5)
entrada_numero1 = tk.Entry(janela)
entrada_numero1.pack()

tk.Label(janela, text="Segundo Numero:").pack(pady=5)
entrada_numero2 = tk.Entry(janela)
entrada_numero2.pack()

# Dropdown de operações
operacao_selecionada = tk.StringVar()
operacao_selecionada.set("+")  # operação padrão
operacao_selecionada.trace("w", atualizar_campos)

operacoes = ["+", "-", "*", "/", "^", "sen", "cos", "tang", "√"]
tk.Label(janela, text="Selecione a operação:").pack(pady=5)
tk.OptionMenu(janela, operacao_selecionada, *operacoes).pack()

# Botão de calcular
tk.Button(janela, text="Calcular", command=calcular).pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="",font=("Arial", 12))
label_resultado.pack(pady=10)

# Inicializa o estado do campo segundo número
atualizar_campos()

janela.mainloop()