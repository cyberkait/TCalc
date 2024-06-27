"""
Functions for working with console menus.
"""

def testInput(inp, menu):
    """
    Evaluates whether a string could be an option in the menu.
    """
    try:
        num = int(inp)
    except:
        items = [option for option in menu if option[:len(inp)] == inp]
        if len(items) > 1:
            print("Multiple results found. Please enter the number matching your result: ")
            for num, item in enumerate(items, start=1):
                print(f"{num}. {item}")
            clarifying = True
            while clarifying:
                try:
                    new = int(input())
                except:
                    print("Must enter a number.")
                else:
                    if num < 0 or num > len(items):
                        print("Invalid choice.")
                    else:
                        return items[new-1]
                    clarifying = False
        elif len(items) == 1:
            return items[0]
    else:
        if num <= len(menu) and num > 0:
            return menu[num-1]

def get_menu_choice(options):
    """
    Gets the user's choice from the menu.
    """
    print("Please select an option:")
    for num, option in enumerate(options, start=1):
        print(f"{num}. {option}")
    typing = True
    while typing:
        user_input = input().lower()
        if (result := testInput(user_input, options)) != "":
            return result
            typing = False
        else:
            print("Invalid selection.")

