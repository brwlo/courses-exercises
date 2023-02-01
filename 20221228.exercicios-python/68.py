from random import randint
print("JOGO DE PAR OU ÍMPAR")
vitorias = 0
while True:
    jogador = computador = " "
    while jogador not in "pPiI":
        jogador = input("PAR OU ÍMPAR? (p/i)").strip().lower()[0]
    jogaescolha = int(input("      você: "))
    compescolha = randint(0,11)
    print(f"computador: {compescolha}")
    resultado = jogaescolha + compescolha
    print(f" resultado: {resultado}")
    parouimpar = "i" if resultado % 2 != 0 else "p"
    if jogaescolha == compescolha:
        print(10*"=","empate",10*"=")
    elif jogador == parouimpar:
        vitorias += 1
        print(10*"=","ganhou",10*"=")
    elif jogaescolha != parouimpar:
        print(10*"=","perdeu",10*"=")
        print(f"VITÓRIAS: {vitorias}")
        break

