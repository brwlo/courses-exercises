print("taboada de n até que n seja < 0")
while True:
    n = int(input("n = "))
    if n < 0:
        break
    for c in range(0,11):
        print(f"{n} x {c} = {n*c}")

