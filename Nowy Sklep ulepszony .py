x = ("x1","x2","x3","x4")
koszyk = []
w = input("Czy chcesz wejść do sklepu?")
if w == "Tak":
     print("~Wszedłeś do sklepu")
else:
     print("Poszedłeś dalej")

if w == "Tak":
    print("Podchodzi do Ciebie pani ekspedientka ")
    print("Podać coś dla pana?")
    print("Dzisiaj mamy bardzo mało towaru ale napewno coś dla Ciebie sie znajdzie ! :)")
    print("Wybierz coś a dodam Ci coś do koszyka!")

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
else:
    print("W takim razie co chcesz zrobić?")

