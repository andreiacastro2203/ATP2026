import random
def computador_pensa():
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    acertou = False

    print("\nPensei num número entre 0 e 100. Tenta adivinhar!")

    while not acertou:
        palpite = int(input("O teu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            acertou = True
            print(f"Acertou! Usaste {tentativas} tentativa(s).")
        elif palpite < numero_secreto:
            print("O número que pensei é Maior")
        else:
            print("O número que pensei é Menor")
def utilizador_pensa():
    limite_inferior = 0
    limite_superior = 100
    tentativas = 0
    acertou = False

    print("\nPensa num número entre 0 e 100. Eu vou tentar adivinhar!")
    print("Responde com: 'Acertou', 'Maior' ou 'Menor'.")

    while not acertou:
        palpite = (limite_inferior + limite_superior) // 2
        tentativas += 1

        resposta = input(f"O meu palpite é {palpite}. O que dizes? ").strip().lower()

        if resposta == "acertou":
            acertou = True
            print(f"Consegui! Usei {tentativas} tentativa(s).")
        elif resposta == "maior":
            limite_inferior = palpite + 1
        elif resposta == "menor":
            limite_superior = palpite - 1
        else:
            print("Resposta inválida. Usa 'Acertou', 'Maior' ou 'Menor'.")
            tentativas -= 1  # não conta tentativas inválidas
def main():
    print("=== Adivinha o Número ===")
    print("1 - O computador pensa num número, tu adivinhas")
    print("2 - Tu pensas num número, o computador adivinha")

    opcao = input("Escolhe uma opção (1 ou 2): ")

    if opcao == "1":
        computador_pensa()
    elif opcao == "2":
        utilizador_pensa()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()