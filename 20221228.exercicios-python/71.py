cinquenta = vinte = dez = um = 0
val = int(input("sacar quanto? "))
while val >= 50:
   val -= 50
   cinquenta += 1
while val >= 20:
    val -= 20
    vinte += 1
while val >= 10:
    val -= 10
    dez += 1
while val >= 1:
    val -= 1
    um += 1
print(f"notas de cinquenta: {cinquenta}")
print(f"    notas de vinte: {vinte}")
print(f"      notas de dez: {dez}")
print(f"       notas de um: {um}")

