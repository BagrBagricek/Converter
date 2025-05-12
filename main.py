def GetOption():
    print("1. Měna")
    print("2. Vzdálenost")
    print("3. Hmotnost")
    print("4. Energie")
    print("5. Exit")
    option = input("Zadejte číslo volby: ")
    try:
        option = int(option)
    except ValueError:
        print("Neplatný vstup. Zadejte číslo.")
        return GetOption()
    match option:
        case 1:
            Currency()
        case 2:
            Distance()
        case 3:
            Weight()
        case 4:
            Energy()
        case 5:
            exit()
        case _:
            print("Neplatná volba. Zadejte číslo mezi 1 a 5.")
            return GetOption()

def Currency():
    print("Vybrali jste měnu.")
    print("1. CZK -> EUR")
    print("2. CZK -> USD")
    print("3. EUR -> CZK")
    print("4. EUR -> USD")
    print("5. USD -> CZK")
    print("6. USD -> EUR")
    print("7. Zpět do hlavního menu")
    print("8. Konec")

    option = input("Zadejte číslo volby: ")
    try:
        option = int(option)
    except ValueError:
        print("Neplatný vstup. Zadejte číslo.")
        return Currency()
    match option:
        case 1:
            holder = input("Zadejte částku v CZK: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Currency()
            if holder < 0:
                print("Částka musí být kladná.")
                Currency()
            else:
                print(f"{holder} CZK = {holder * 0.042} EUR \n")
                Currency()
        case 2:
            holder = input("Zadejte částku v CZK: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Currency()
            if holder < 0:
                print("Částka musí být kladná.")
                Currency()
            else:
                print(f"{holder} CZK = {holder * 0.045} USD \n")
                Currency()
        case 3:
            holder = input("Zadejte částku v EUR: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Currency()
            if holder < 0:
                print("Částka musí být kladná.")
                Currency()
            else:
                print(f"{holder} EUR = {holder * 23.81} CZK \n")
                Currency()
        case 4:
            holder = input("Zadejte částku v EUR: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Currency()
            if holder < 0:
                print("Částka musí být kladná.")
                Currency()
            else:
                print(f"{holder} EUR = {holder * 1.08} USD \n")
                Currency()
        case 5:
            holder = input("Zadejte částku v USD: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Currency()
            if holder < 0:
                print("Částka musí být kladná.")
                Currency()
            else:
                print(f"{holder} USD = {holder * 22.22} CZK \n")
                Currency()
        case 6:
            holder = input("Zadejte částku v USD: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Currency()
            if holder < 0:
                print("Částka musí být kladná.")
                Currency()
            else:
                print(f"{holder} USD = {holder * 0.93} EUR \n")
                Currency()
        case 7:
            GetOption()
        case 8:
            exit()
        case _:
            print("Neplatná volba. Zadejte číslo mezi 1 a 6.")
            return Currency()
def Distance():
    print("Vybrali jste vzdálenost.")
    print("1. Loket -> Sáh")
    print("2. Loket -> Palec")
    print("3. Loket -> Píď")
    print("4. Loket -> Stopa")
    print("\n5. Sáh -> Loket")
    print("6. Sáh -> Palec")
    print("7. Sáh -> Píď")
    print("8. Sáh -> Stopa")
    print("\n9. Palec -> Loket")
    print("10. Palec -> Sáh")
    print("11. Palec -> Píď")
    print("12. Palec -> Stopa")
    print("\n13. Píď -> Loket")
    print("14. Píď -> Sáh")
    print("15. Píď -> Palec")
    print("16. Píď -> Stopa")
    print("\n17. Stopa -> Loket")
    print("18. Stopa -> Sáh")
    print("19. Stopa -> Palec")
    print("20. Stopa -> Píď")
    print("\n21. Zpět do hlavního menu")
    print("22. Konec")
    option = input("Zadejte číslo volby: ")
    try:
        option = int(option)
    except ValueError:
        print("Neplatný vstup. Zadejte číslo.")
        return Distance()
    match option:
        case 1:
            holder = input("Zadejte vzdálenost v loktech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} loket = {holder * 0.5} sáh \n")
                Distance()
        case 2:
            holder = input("Zadejte vzdálenost v loktech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} loket = {holder * 12} palec \n")
                Distance()
        case 3:
            holder = input("Zadejte vzdálenost v loktech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} loket = {holder * 6} píď \n")
                Distance()
        case 4:
            holder = input("Zadejte vzdálenost v loktech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} loket = {holder * 3} stopa \n")
                Distance()
        case 5:
            holder = input("Zadejte vzdálenost v sáhách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} sáh = {holder * 2} loket \n")
                Distance()
        case 6:
            holder = input("Zadejte vzdálenost v sáhách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} sáh = {holder * 24} palec \n")
                Distance()
        case 7:
            holder = input("Zadejte vzdálenost v sáhách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} sáh = {holder * 12} píď \n")
                Distance()
        case 8:
            holder = input("Zadejte vzdálenost v sáhách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} sáh = {holder * 6} stopa \n")
                Distance()
        case 9:
            holder = input("Zadejte vzdálenost v palcích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} palec = {holder * 0.0833} loket \n")
                Distance()
        case 10:
            holder = input("Zadejte vzdálenost v palcích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} palec = {holder * 0.0417} sáh \n")
                Distance()
        case 11:
            holder = input("Zadejte vzdálenost v palcích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} palec = {holder * 0.5} píď \n")
                Distance()
        case 12:
            holder = input("Zadejte vzdálenost v palcích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} palec = {holder * 0.0833} stopa \n")
                Distance()
        case 13:
            holder = input("Zadejte vzdálenost v píďkách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} píď = {holder * 0.1667} loket \n")
                Distance()
        case 14:
            holder = input("Zadejte vzdálenost v píďkách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} píď = {holder * 0.0833} sáh \n")
                Distance()
        case 15:
            holder = input("Zadejte vzdálenost v píďkách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} píď = {holder * 2} palec \n")
                Distance()
        case 16:
            holder = input("Zadejte vzdálenost v píďkách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} píď = {holder * 0.3333} stopa \n")
                Distance()
        case 17:
            holder = input("Zadejte vzdálenost ve stopách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} stopa = {holder * 0.3333} loket \n")
                Distance()
        case 18:
            holder = input("Zadejte vzdálenost ve stopách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} stopa = {holder * 0.1667} sáh \n")
                Distance()
        case 19:
            holder = input("Zadejte vzdálenost ve stopách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} stopa = {holder * 12} palec \n")
                Distance()
        case 20:
            holder = input("Zadejte vzdálenost ve stopách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Distance()
            if holder < 0:
                print("Vzdálenost musí být kladná.")
                Distance()
            else:
                print(f"{holder} stopa = {holder * 3} píď \n")
                Distance()
        case 21:
            GetOption()
        case 22:
            exit()


def Weight():
    print("Vybrali jste hmotnost.")
    print("1. Gram -> Libra")
    print("2. Gram -> Unce")
    print("3. Gram -> Kilogram")
    print("4. Gram -> Kámen")
    print("\n5. Libra -> Gram")
    print("6. Libra -> Unce")
    print("7. Libra -> Kilogram")
    print("8. Libra -> Kámen")
    print("\n9. Unce -> Gram")
    print("10. Unce -> Libra")
    print("11. Unce -> Kilogram")
    print("12. Unce -> Kámen")
    print("\n13. Kilogram -> Gram")
    print("14. Kilogram -> Libra")
    print("15. Kilogram -> Unce")
    print("16. Kilogram -> Kámen")
    print("\n17. Kámen -> Gram")
    print("18. Kámen -> Libra")
    print("19. Kámen -> Unce")
    print("20. Kámen -> Kilogram")
    print("\n21. Zpět do hlavního menu")
    print("22. Konec")
    option = input("Zadejte číslo volby: ")
    try:
        option = int(option)
    except ValueError:
        print("Neplatný vstup. Zadejte číslo.")
        return Weight()
    match option:
        case 1:
            holder = input("Zadejte hmotnost v gramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} gram = {holder * 0.00220462} libra \n")
                Weight()
        case 2:
            holder = input("Zadejte hmotnost v gramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} gram = {holder * 0.035274} unce \n")
                Weight()
        case 3:
            holder = input("Zadejte hmotnost v gramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} gram = {holder * 0.001} kilogram \n")
                Weight()
        case 4:
            holder = input("Zadejte hmotnost v gramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} gram = {holder * 0.00015747} kámen \n")
                Weight()
        case 5:
            holder = input("Zadejte hmotnost v librách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} libra = {holder * 453.592} gram \n")
                Weight()
        case 6:
            holder = input("Zadejte hmotnost v librách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} libra = {holder * 16} unce \n")
                Weight()
        case 7:
            holder = input("Zadejte hmotnost v librách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} libra = {holder * 0.453592} kilogram \n")
                Weight()
        case 8:
            holder = input("Zadejte hmotnost v librách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} libra = {holder * 0.0714286} kámen \n")
                Weight()
        case 9:
            holder = input("Zadejte hmotnost v uncích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} unce = {holder * 28.3495} gram \n")
                Weight()
        case 10:
            holder = input("Zadejte hmotnost v uncích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} unce = {holder * 0.0625} libra \n")
                Weight()
        case 11:
            holder = input("Zadejte hmotnost v uncích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} unce = {holder * 0.0283495} kilogram \n")
                Weight()
        case 12:
            holder = input("Zadejte hmotnost v uncích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} unce = {holder * 0.00446429} kámen \n")
                Weight()
        case 13:
            holder = input("Zadejte hmotnost v kilogramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kilogram = {holder * 1000} gram \n")
                Weight()
        case 14:
            holder = input("Zadejte hmotnost v kilogramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kilogram = {holder * 2.20462} libra \n")
                Weight()
        case 15:
            holder = input("Zadejte hmotnost v kilogramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kilogram = {holder * 35.274} unce \n")
                Weight()
        case 16:
            holder = input("Zadejte hmotnost v kilogramech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kilogram = {holder * 0.157473} kámen \n")
                Weight()
        case 17:
            holder = input("Zadejte hmotnost v kamenech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kámen = {holder * 6350.29} gram \n")
                Weight()
        case 18:
            holder = input("Zadejte hmotnost v kamenech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kámen = {holder * 140} libra \n")
                Weight()
        case 19:
            holder = input("Zadejte hmotnost v kamenech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kámen = {holder * 2240} unce \n")
                Weight()
        case 20:
            holder = input("Zadejte hmotnost v kamenech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Weight()
            if holder < 0:
                print("Hmotnost musí být kladná.")
                Weight()
            else:
                print(f"{holder} kámen = {holder * 6.35029} kilogram \n")
                Weight()
        case 21:
            GetOption()
        case 22:
            exit()
def Energy():
    print("Vybrali jste energii.")
    print("1. Joule -> Kalorie")
    print("2. Joule -> Elektronvolt")
    print("3. Joule -> Killowatthodina")
    print("\n4. Kalorie -> Joule")
    print("5. Kalorie -> Elektronvolt")
    print("6. Kalorie -> Killowatthodina")
    print("\n7. Elektronvolt -> Joule")
    print("8. Elektronvolt -> Kalorie")
    print("9. Elektronvolt -> Killowatthodina")
    print("\n10. Killowatthodina -> Joule")
    print("11. Killowatthodina -> Kalorie")
    print("12. Killowatthodina -> Elektronvolt")
    print("\n13. Zpět do hlavního menu")
    print("14. Konec")
    option = input("Zadejte číslo volby: ")
    try:
        option = int(option)
    except ValueError:
        print("Neplatný vstup. Zadejte číslo.")
        return Energy()
    match option:
        case 1:
            holder = input("Zadejte energii v Joulech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Joule = {holder * 0.239006} Kalorie \n")
                Energy()
        case 2:
            holder = input("Zadejte energii v Joulech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Joule = {holder * 6.242e+18} Elektronvolt \n")
                Energy()
        case 3:
            holder = input("Zadejte energii v Joulech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Joule = {holder * 2.77778e-7} Killowatthodina \n")
                Energy()
        case 4:
            holder = input("Zadejte energii v Kaloriích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Kalorie = {holder * 4.184} Joule \n")
                Energy()
        case 5:
            holder = input("Zadejte energii v Kaloriích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Kalorie = {holder * 2.611e+19} Elektronvolt \n")
                Energy()
        case 6:
            holder = input("Zadejte energii v Kaloriích: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Kalorie = {holder * 1.16222e-6} Killowatthodina \n")
                Energy()
        case 7:
            holder = input("Zadejte energii v Elektronvoltech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Elektronvolt = {holder * 1.60218e-19} Joule \n")
                Energy()
        case 8:
            holder = input("Zadejte energii v Elektronvoltech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Elektronvolt = {holder * 3.8e-14} Kalorie \n")
                Energy()
        case 9:
            holder = input("Zadejte energii v Elektronvoltech: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Elektronvolt = {holder * 3.6e-22} Killowatthodina \n")
                Energy()
        case 10:
            holder = input("Zadejte energii v Killowatthodinách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Killowatthodina = {holder * 3.6e+6} Joule \n")
                Energy()
        case 11:
            holder = input("Zadejte energii v Killowatthodinách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Killowatthodina = {holder * 860421} Kalorie \n")
                Energy()
        case 12:
            holder = input("Zadejte energii v Killowatthodinách: ")
            try:
                holder = float(holder)
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")
                return Energy()
            if holder < 0:
                print("Energie musí být kladná.")
                Energy()
            else:
                print(f"{holder} Killowatthodina = {holder * 2.25e+25} Elektronvolt \n")
                Energy()
        case 13:
            GetOption()
        case 14:
            exit()

GetOption()