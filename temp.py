koszykUzytkownika = []
czyDalejRobieZakupy = True
asortyment = ["Mleko","Chleb","Masło","Kurczak","Jajka","Ogorek","Pomidor","Cukierki","Szynka"]

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
    if wybranyPrzedmiot in asortyment:
        koszykUzytkownika.append(wybranyPrzedmiot)
    else:
        print("Wpierdol. W asortymencie nie ma takiego itemku")

def pokazKoszyk():
    print("Teraz twoj koszyk zawiera:")
    print(koszykUzytkownika)

def usun():
    print("Co chcesz usunąć?")

    wybranyPrzedmiot = input()
    if wybranyPrzedmiot in koszykUzytkownika:
        koszykUzytkownika.remove(wybranyPrzedmiot)
    else:
        print("Wpierdol. W koszyku nie ma takiego itemku")


while czyDalejRobieZakupy:
    wyborUzytkownika = menu()
    if wyborUzytkownika == '1':
        kup()
        pokazKoszyk()

    elif wyborUzytkownika == '2':
        pokazKoszyk()
        usun()

    elif wyborUzytkownika == '3':
        pokazKoszyk()


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
