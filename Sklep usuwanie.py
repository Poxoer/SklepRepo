koszyk = ["x1","x2","x3"]
k = input("Czy chcial byś zobaczyć zawartość swojego koszyka?")
if k == "tak" or k == "Tak":
     print(koszyk)
p = input("Czy chcesz usunąć coś z koszyka?")
if p == "Tak":
    while True:
        b = input("Co chcesz usunąć?")

        if b == "x1":

            if ("x1" in koszyk):
                koszyk.remove("x1")
                print("Usunięto produkt")
                print("Twój aktulany stan koszyka to: ")
                print(koszyk)
        if b == "x2":

            if ("x2" in koszyk):
                koszyk.remove("x2")
                print("Usunięto produkt")
                print("Twój aktulany stan koszyka to: ")
                print(koszyk)
        if b == "x3":

            if ("x3" in koszyk):
                koszyk.remove("x3")
                print("Usunięto produkt")
                print("Twój aktulany stan koszyka to: ")
                print(koszyk)
        if b == "x4":

            if ("x4" in koszyk):
                koszyk.remove("x4")
                print("Usunięto produkt")
                print("Twój aktulany stan koszyka to: ")
                print(koszyk)
            else:
                print("Nie posiadasz takiego produktu")
                print("Twój aktulany stan koszyka to: ")
                print(koszyk)
        if b == "Nic wiecej":
            break

else:
    print("W takim razie zapraszam do kasy")
