masc = more18 = less20 = 0
cont = "s"
while True:
    if cont not in "sS":
        print(10*"=")
        print(f" PESSOAS MAIORES DE 18 ANOS: {more18}")
        print(f"  TOTAL DE HOMENS COMPUTADO: {masc}")
        print(f"MULHERES MENORES DE 20 ANOS: {less20}")
        break
    sex = " "
    age  = int(input("      AGE: "))
    while sex not in "mfMF":
        sex  = input("SEX (m/f): ")
    if age > 18:
        more18 += 1
    if sex in "mM":
        masc += 1
    if sex in "fF" and age < 20:
        less20 += 1
    cont = input("continuar? (s/n)")
