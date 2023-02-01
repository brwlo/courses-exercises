print("999 pára a execução")
c = s = 0
while True:
    n = int(input("n = "))
    if n == 999:
        break
    s = n + s
    c += 1
print(f"números digitados: {c}")
print(f" soma dos números: {s}")

