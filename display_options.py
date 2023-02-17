


def options():
    print("==============MENU===============")
    print("1. VIEW Prehled objednavek")
    print("2. VIEW Objednavky uzivatele")
    print("3. Display data from table")
    print("4. Insert data into table")
    print("5. Delete data from table")
    print("6. Update data from table")
    print("7. Import CSV to table")
    print("8. EXIT")
    print("=================================")
    choice = int(input("Enter your choice: "))
    print("=================================")
    return choice

"""
Tento kod definuje funkci options(), která vypisuje uživateli menu s možnostmi volby,
jako například zobrazit prehled objednávek, vložit data do tabulky, atd. 
Uživatel může vybrat volbu vložením čísla odpovídajícího volby do konzole a funkce options() 
vrátí tuto volbu jako celočíselnou hodnotu.
"""
