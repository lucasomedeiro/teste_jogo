import random
import sys

MIN, MAX, TENTATIVAS = 1, 100, 7


def main():
    # Modo teste: "python adivinha.py 42" faz o numero secreto ser 42
    if len(sys.argv) > 1:
        segredo = int(sys.argv[1])
    else:
        segredo = random.randint(MIN, MAX)

    print("=== ADIVINHE O NUMERO (1 a 100) ===")
    print(f"Voce tem {TENTATIVAS} tentativas.")

    usadas = 0
    while usadas < TENTATIVAS - 1:
        texto = input("Seu palpite: ").strip()
        if not texto.lstrip("-").isdigit():
            print("Digite apenas numeros!")
            continue
        palpite = int(texto)
        usadas += 1
        if palpite <= MIN or palpite >= MAX:
            print("Numero fora do intervalo!")
            continue
        if palpite == segredo:
            print(f"Parabens! Voce acertou em {usadas} tentativa(s)!")
            return
        elif palpite < segredo:
            print("Maior!")
        else:
            print("Menor!")
    print(f"Game Over! O numero era {segredo}.")


main()
