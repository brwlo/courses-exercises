# ignores whether two things are equally cheap
# only the last cheap item is printed
total = cheap = expen = 0
thecheap = ""
while True:
    prod = input("produto: ")
    prec = float(input("preço: "))
    if prec < cheap:
        thecheap = ""
    cheap = prec if cheap == 0 else cheap
    cheap = prec if prec <= cheap else cheap
    if cheap == prec:
        thecheap += " " + prod
    expen = expen + 1 if prec > 1000 else expen
    total += prec
    goon = input("continua? (s/x)")
    if goon not in "sS":
        print(f"total: {total}")
        print(f"caros: {expen} (mais de R$ 1000)")
        print(f"mais baratos: {thecheap}")
        break

