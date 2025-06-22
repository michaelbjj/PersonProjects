print("Verificar se a Palavra é Palíndromo")

word    = input("Digite o palavra: ")
wordaux = word
word1   = ""

for elemento in reversed(word):
    word1 = word1 + "" + elemento  

if word1 == wordaux:
    print("É Palindromo")
else :
    print("Não é Palindromo")
