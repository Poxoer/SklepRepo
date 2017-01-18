koszyk = []
def menu():
    print("Podchodzi do Ciebie pani ekspedientka ")
    print("Dzisiaj mamy bardzo mało towaru ale napewno coś dla Ciebie sie znajdzie ! :)")
    print("Zdecyduj co chcesz zrobić!")
    print("1. Dodaj do koszyka")
    print("2. Usun z Koszyka")
    print("3. Sprawdz co masz w koszyku")
    print("4. Wyjdz ze sklepu")
    return("Copyright. Wykonane przez Jakuba Łagowskiego")

def menu2():
    print("Co chcesz zrobić teraz?")
    print("1. Dodaj do koszyka")
    print("2. Usun z Koszyka")
    print("3. Sprawdz co masz w koszyku")
    print("4. Wyjdz ze sklepu")
    return("Copyright. Wykonane przez Jakuba Łagowskiego")

def kup():
    x = ["x1", "x2", "x3", "x4"]
    while True:
        ans = input(x)
        if ans == "x1":
            koszyk.append("x1")
            print("Dodałes do koszyka produkt x1.")

        elif ans == "x2":
            koszyk.append("x2")
            print("Dodałes do koszyka produkt x2.")

        elif ans == "x3":
            koszyk.append("x3")
            print("Dodałes do koszyka produkt x3.")

        elif ans == "x4":
            koszyk.append("x4")
            print("Dodałes do koszyka produkt x4.")

        elif ans == "Dziekuje":
            print("Zrezygnowałeś z dalszych zakupów")
            break

        else:
            print("Przepraszam, nie posiadam takiego towaru, Nie podoba sie to nie")
            break

    return("Copyright. Wykonane przez Jakuba Łagowskiego")

def usun():
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
                print(menu2())
                break

    else:
        print("W takim razie zapraszam do kasy")
        print(menu2())
    return("Copyright. Wykonane przez Jakuba Łagowskiego")



print(menu())
operacja = input("Co zamierzasz zrobić?")





if operacja == "1": print(kup())
if operacja == "2": print(usun())

# A powinno mi sie menu otworzyc tak dokladnie menu2