koszykUzytkownika = []
czyDalejRobieZakupy = True
asortyment = ["Mleko","Chleb","Masło","Kurczak","Jajka","Ogorek","Pomidor","Cukierki","Szynka"]

def czyJestWasortymencie(item):
    if item in asortyment:
        return True
    else:
        return False


def menu():
    print("Co chcesz zrobić?")
    print("1. Dodaj do koszyka")
    print("2. Usun z koszyka")
    print("3. Sprawdz co masz w koszyku")
    print("4. Wyjdz ze sklepu")
    return input()

def kup():
    print("Co chcesz dodac?")

    wybranyPrzedmiot = input()
    # obczaj tutaj wybierasz indeks elementu z tablicy od uzytkownika
    # masz tablice asortyment ktora ma od 0 do n elementow.
    # musisz sprawdzic jaka liczbe podal uzytkownik i dodac element o wybranym indeksie do koszyka, prosta sprawa
    # jedyne co sprawdzasz to czy podany indeks nie jest wiekszy niz wielkosc tablicy
    # czaisz?Nom 3/4 ale coś tak
    # no tylko teraz jest tak, ze to co pobierasz od uzytkownika to tekst dlatego wyjebal sie blad
    # trzeba tekst zamienic na liczbe
    if czyJestWasortymencie(wybranyPrzedmiot):
        koszykUzytkownika.append(wybranyPrzedmiot)
    else:
        print("Wpierdol. W asortymencie nie ma takiego itemku")

    # dlug = len(asortyment)
    # for i in range(dlug):
    #     if wybranyPrzedmiot == asortyment[i]:
    #         koszykUzytkownika.append(wybranyPrzedmiot)
    #         break
    #     elif wybranyPrzedmiot != asortyment[i]:
    #         continue
    #     elif i == dlug:
    #         print("Wpierdol. W asortymencie nie ma takiego itemku")

def pokazKoszyk():
    print("Teraz twoj koszyk zawiera:")
    print(koszykUzytkownika)

def usun():
    print("Co chcesz usunąć?")
    #todo pomyśleć jak wykonać
    #- Usuwanie z koszyka
    #- Odmowe usuwania z koszyka jeżeli produkt nie znajduje sie w koszyku
    #- Poszukać w Internecie jak to wykonać XD


while czyDalejRobieZakupy:
    wyborUzytkownika = menu()
    if wyborUzytkownika == '1':
        kup()
        pokazKoszyk()

    elif wyborUzytkownika == '2':
        pokazKoszyk()
        usun()



    elif wyborUzytkownika == '3':

        print("not implemented yet")

    elif wyborUzytkownika == '4':
        czyDalejRobieZakupy = False

print("Twój koszyk")
print(pokazKoszyk())
print("Dowidzenia")

#Słowa od Profesora M.Ł
#Pokrzepiające dusze oraz motywujące
#"a tak pozatym to bardzo dobrze CI idzie ziomeczku"
#TODO WYKONAC ASORTYMENT SKLEPU ; CENNIK i SUME ZAKUPÓW
#TODO XD
