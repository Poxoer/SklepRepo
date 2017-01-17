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
    print("Wybierz coś a dodam Ci do koszyka!")
    ans = input(x)
    while ans == ("x1","x2","x3","x4"):
        if ans == "x1":
            koszyk.append("x3")

        elif ans == "x2":
            koszyk.append("x2")

        elif ans == "x3":
            koszyk.append("x3")

        elif ans == "x4":
            koszyk.append("x4")

        else:
            print("Przepraszam, nie posiadam takiego towaru, wybierz ponownie")
