def perform_conversion(amount, factor, from_unit, to_unit):
    """Performs the conversion and returns the result string."""
    return f"{amount} {from_unit} = {amount * factor} {to_unit} \n"

def get_float_input(prompt):
    """Gets a float input from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Hodnota musí být kladná.")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")

def handle_category(category_name, conversion_options):
    """Handles the conversions within a specific category."""
    print(f"Vybrali jste {category_name}.")
    for key, (from_unit, to_unit, _) in conversion_options.items():
        print(f"{key}. {from_unit} -> {to_unit}")
    print(f"{len(conversion_options) + 1}. Zpět do hlavního menu")
    print(f"{len(conversion_options) + 2}. Konec")

    while True:
        option = input("Zadejte číslo volby: ")
        try:
            option = int(option)
            if 1 <= option <= len(conversion_options):
                from_unit, to_unit, factor = conversion_options[option]
                amount = get_float_input(f"Zadejte množství v {from_unit}: ")
                print(perform_conversion(amount, factor, from_unit, to_unit))
            elif option == len(conversion_options) + 1:
                return  # Go back to the main menu
            elif option == len(conversion_options) + 2:
                exit()
            else:
                print(f"Neplatná volba. Zadejte číslo mezi 1 a {len(conversion_options) + 2}.")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")

def GetOption():
    """Displays the main menu and handles category selection."""
    main_menu = {
        1: {"name": "Měna", "options": {
            1: ("CZK", "EUR", 0.042),
            2: ("CZK", "USD", 0.045),
            3: ("EUR", "CZK", 23.81),
            4: ("EUR", "USD", 1.08),
            5: ("USD", "CZK", 22.22),
            6: ("USD", "EUR", 0.93),
        }},
        2: {"name": "Vzdálenost", "options": {
            1: ("Loket", "Sáh", 0.5),
            2: ("Loket", "Palec", 12),
            3: ("Loket", "Píď", 6),
            4: ("Loket", "Stopa", 3),
            5: ("Sáh", "Loket", 2),
            6: ("Sáh", "Palec", 24),
            7: ("Sáh", "Píď", 12),
            8: ("Sáh", "Stopa", 6),
            9: ("Palec", "Loket", 0.0833),
            10: ("Palec", "Sáh", 0.0417),
            11: ("Palec", "Píď", 0.5),
            12: ("Palec", "Stopa", 0.25),
            13: ("Píď", "Loket", 0.1667),
            14: ("Píď", "Sáh", 0.0833),
            15: ("Píď", "Palec", 2),
            16: ("Píď", "Stopa", 0.5),
            17: ("Stopa", "Loket", 0.3333),
            18: ("Stopa", "Sáh", 0.1667),
            19: ("Stopa", "Palec", 12),
            20: ("Stopa", "Píď", 3),
        }},
        3: {"name": "Hmotnost", "options": {
            1: ("Gram", "Libra", 0.00220462),
            2: ("Gram", "Unce", 0.035274),
            3: ("Gram", "Kilogram", 0.001),
            4: ("Gram", "Kámen", 0.00015747),
            5: ("Libra", "Gram", 453.592),
            6: ("Libra", "Unce", 16),
            7: ("Libra", "Kilogram", 0.453592),
            8: ("Libra", "Kámen", 0.0714286),
            9: ("Unce", "Gram", 28.3495),
            10: ("Unce", "Libra", 0.0625),
            11: ("Unce", "Kilogram", 0.0283495),
            12: ("Unce", "Kámen", 0.00446429),
            13: ("Kilogram", "Gram", 1000),
            14: ("Kilogram", "Libra", 2.20462),
            15: ("Kilogram", "Unce", 35.274),
            16: ("Kilogram", "Kámen", 0.157473),
            17: ("Kámen", "Gram", 6350.29),
            18: ("Kámen", "Libra", 14),
            19: ("Kámen", "Unce", 224),
            20: ("Kámen", "Kilogram", 6.35029),
        }},
        4: {"name": "Energie", "options": {
            1: ("Joule", "Kalorie", 0.239006),
            2: ("Joule", "Elektronvolt", 6.242e+18),
            3: ("Joule", "Killowatthodina", 2.77778e-7),
            4: ("Kalorie", "Joule", 4.184),
            5: ("Kalorie", "Elektronvolt", 2.611e+19),
            6: ("Kalorie", "Killowatthodina", 1.16222e-6),
            7: ("Elektronvolt", "Joule", 1.60218e-19),
            8: ("Elektronvolt", "Kalorie", 3.8e-20),
            9: ("Elektronvolt", "Killowatthodina", 4.4505e-26),
            10: ("Killowatthodina", "Joule", 3.6e+6),
            11: ("Killowatthodina", "Kalorie", 860421),
            12: ("Killowatthodina", "Elektronvolt", 2.24694e+25),
        }},
        5: "Exit"
    }

    print("Vyberte kategorii:")
    for key, value in main_menu.items():
        if key != 5:
            print(f"{key}. {value['name']}")
        else:
            print(f"{key}. {value}")

    while True:
        option = input("Zadejte číslo volby: ")
        try:
            option = int(option)
            if option in main_menu:
                if option == 5:
                    exit()
                else:
                    selected_category = main_menu[option]
                    handle_category(selected_category["name"], selected_category["options"])
            else:
                print("Neplatná volba. Zadejte číslo mezi 1 a 5.")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")

if __name__ == "__main__":
    GetOption()