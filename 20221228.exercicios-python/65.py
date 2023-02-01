opcao = ""
menor = 0
maior = 0
total = 0
conta = 0
valor = 0
while opcao in "sS":
    valor = int(input("n = "))
    if conta == 0:
        maior = menor = valor
    maior = max(valor,maior)
    menor = min(valor,menor)
    conta = conta + 1
    total = total + valor
    opcao = input("mais (s/n)? ")
media = total / conta
print(10*"=")
print("maior: ",maior)
print("menor: ",menor)
print("média: ",media)

