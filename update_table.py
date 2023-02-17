
"""
Tento kód umožňuje uživateli aktualizovat hodnoty v tabulkách "Uživatel" a "Produkt".
Uživatel nejprve vybere tabulku, v níž chce provést změnu, a následně zadá ID záznamu, který chce aktualizovat. Poté mu script nabídne možnosti sloupců,
které lze aktualizovat a po výběru sloupce se uživateli zobrazí stará hodnota a požádá ho o zadání nové hodnoty. Nakonec dojde k aktualizaci dat v databázi.
"""

def update(cnx):
    cursor = cnx.cursor()
    print("1. Uzivatel")
    print("2. Produkt")
    choice_table = int(input("V jake tabulce chcete provadet zmenu? (zadejte cislo 1 nebo 2): "))
    if choice_table == 1:
        table = "Uzivatel"
        columns = ["Jmeno", "Prijmeni", "Email", "Datum_nar"]
    elif choice_table == 2:
        table = "Produkt"
        columns = ["Nazev", "Barva", "Rozmer", "Dostupnost", "Cena"]
    else:
        print("Neplatna volba tabulky.")
        return
    record_id = int(input("Zadejte ID zaznamu, ktery chcete aktualizovat: "))
    print("Co chcete aktualizovat?")
    for i, column in enumerate(columns):
        print(f"{i + 1}. {column}")
    choice_column = int(input("Zadejte cislo polozky, kterou chcete aktualizovat: "))
    if choice_column < 1 or choice_column > len(columns):
        print("Neplatna volba polozky.")
        return
    column = columns[choice_column - 1]
    query = f"SELECT {column} FROM {table} WHERE ID = {record_id}"
    cursor.execute(query)
    old_value = cursor.fetchone()[0]
    new_value = input(f"Zadejte novou hodnotu pro {column} (puvodni hodnota: {old_value}): ")
    query = f"UPDATE {table} SET {column} = '{new_value}' WHERE ID = {record_id}"
    cursor.execute(query)
    cnx.commit()
    print("Data updated successfully.")