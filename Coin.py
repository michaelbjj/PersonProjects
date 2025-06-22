# Conversor de Moedas Simples
#https://app.exchangerate-api.com/activate-account

# Dicionário com taxas de câmbio fixas em relação ao dólar americano (USD)
import requests

def converter_moeda(valor, de, para, chave_api):
    url = f"https://v6.exchangerate-api.com/v6/{chave_api}/pair/{de}/{para}/{valor}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return "Erro ao acessar a API." 

    dados = resposta.json()

    if dados['result'] == 'success':
        return dados['conversion_result']
    else:
        return "Erro na conversão."

# Interface
print("=== Conversor de Moedas (Tempo Real) ===")
chave_api = input("Digite sua chave da ExchangeRate API: ")
de = input("Converter de (ex: BRL): ").upper()
para = input("Converter para (ex: USD): ").upper()
valor = float(input(f"Valor em {de}: "))

resultado = converter_moeda(valor, de, para, chave_api)

if isinstance(resultado, float):
    print(f"{valor:.2f} {de} = {resultado:.2f} {para}")
else:
    print("Erro:", resultado)
    
#Digite sua chave da ExchangeRate API: 97377ef3a382d8702e3307c2
#Converter de (ex: BRL): BRL
#Converter para (ex: USD): USD
#Valor em BRL: 100
#100.00 BRL = 18.42 USD    