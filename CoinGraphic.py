import tkinter as tk
from tkinter import ttk, messagebox
import requests

#Your API Key: 97377ef3a382d8702e3307c2

# Função para conversão usando API ExchangeRate
def converter():
    chave_api = entry_api.get().strip()
    de = combo_de.get().upper()
    para = combo_para.get().upper()
    try:
        valor = float(entry_valor.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")
        return

    url = f"https://v6.exchangerate-api.com/v6/{chave_api}/pair/{de}/{para}/{valor}" 
    resposta = requests.get(url)

    if resposta.status_code != 200:
        messagebox.showerror("Erro", "Erro ao acessar a API.")
        return

    dados = resposta.json()
    if dados["result"] != "success":
        messagebox.showerror("Erro", "Erro na conversão: Verifique a chave ou moedas.")
        return

    resultado = dados["conversion_result"]
    label_resultado.config(text=f"{valor:.2f} {de} = {resultado:.2f} {para}")

# Lista de moedas mais comuns
moedas = ["USD", "BRL", "EUR", "JPY", "GBP", "CAD", "AUD", "ARS", "CNY"]

# Criar janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas - Tempo Real")
janela.geometry("400x300")
janela.resizable(False, False)

# Campo de chave API
tk.Label(janela, text="Chave da API:").pack(pady=5)
entry_api = tk.Entry(janela, width=40)
entry_api.pack()

# Campo de valor
tk.Label(janela, text="Valor a converter:").pack(pady=5)
entry_valor = tk.Entry(janela)
entry_valor.pack()

# Seleção de moedas
frame_moedas = tk.Frame(janela)
frame_moedas.pack(pady=10)

tk.Label(frame_moedas, text="De:").grid(row=0, column=0, padx=10)
combo_de = ttk.Combobox(frame_moedas, values=moedas, state="readonly")
combo_de.grid(row=0, column=1)

tk.Label(frame_moedas, text="Para:").grid(row=0, column=2, padx=10)
combo_para = ttk.Combobox(frame_moedas, values=moedas, state="readonly")
combo_para.grid(row=0, column=3)

# Botão de conversão
botao = tk.Button(janela, text="Converter", command=converter)
botao.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

janela.mainloop()
