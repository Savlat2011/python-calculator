
Savlat = True
while Savlat:
    a = int(input("1:"))
    b = int(input("2:"))
    us = input("+, -, * or /:")
    if us == "+":
        print(a + b)
        fr = input("Vill du försetta?")
        if fr == " Yes":

            continue
        else:
            break
    if us == "-":
        print(a - b)
        fr = input("Vill du försetta?")
        if fr == " Yes":
            continue
        else:
            break
    if us == "*":
        print(a * b)
        fr = input("Vill du försetta?")
        if fr == " Yes":
            continue
        else:
            break
    if us == "/":
        print(a / b)
        fr = input("Vill du försetta?")
        if fr == " Yes":
            continue
        else:
            break

