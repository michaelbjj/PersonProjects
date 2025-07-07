import random

def jogar_forca():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "internet"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for _ in palavra_secreta]
    tentativas = 6
    letras_erradas = []

    print("=== JOGO DA FORCA ===")

    while tentativas > 0 and "_" in letras_acertadas:
        print("\nPalavra: ", " ".join(letras_acertadas))
        print("Erros: ", ", ".join(letras_erradas))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra!")
            continue

        if ((letra in letras_acertadas) or (letra in letras_erradas)):
            print("Você já tentou essa letra.")
            continue

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_acertadas[i] = letra
            print("Acertou!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Errou!")

    if "_" not in letras_acertadas:
        print("\nParabéns! Você venceu! A palavra era:", palavra_secreta)
    else:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

# Rodar o jogo
jogar_forca()
