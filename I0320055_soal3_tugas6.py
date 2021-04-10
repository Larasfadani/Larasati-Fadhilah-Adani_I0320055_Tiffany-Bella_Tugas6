prima = [11, 13, 17, 19, 23]
for a in range(10, 25):
    if a == 10:
        print(a, "Bukan Prima")
    elif a == 11:
        print(a, "Adalah Bilangan Prima")
    elif a == 13:
        print(a, "Adalah Bilangan Prima")
    elif a == 17:
        print(a, "Adalah Bilangan Prima")
    elif a == 19:
        print(a, "Adalah Bilangan Prima")
    elif a == 23:
        print(a, "Adalah Bilangan Prima")
    else:
        for i in range(2, a):
            if a % i == 0:
                print(a, "Bukan Prima")
                break
        else:
            break