


def display_table(cnx):
    cursor = cnx.cursor()
    result = None
    print("==========TABULKY===========")
    print("1. Uzivatel")
    print("2. Produkt")
    print("3. Pobocka")
    print("4. Zamestnanec")
    print("5. Objednavka")
    print("6. Prace")
    choice_table = int(input("Enter your choice: "))
    print("============================")
    if choice_table == 1:
            print("ID | Jmeno | Prijmeni | Email | Datum Narozeni")
            query = "SELECT * FROM Uzivatel"
    elif choice_table == 2:
            print("ID | Nazev | Barva | Rozmer | Cena | Dostupnost")
            query = "SELECT * FROM Produkt"
    elif choice_table == 3:
            print("ID | Adresa | Cislo popisne | PSC")
            query = "SELECT * FROM Pobocka"
    elif choice_table == 4:
            print("ID | Jmeno | Prijmeni | Zacatek prace")
            query = "SELECT * FROM Zamestnanec"
    elif choice_table == 5:
            print("ID | Datum objednavky | Prosla platba | pobocka_id | uzivatel_id | produkt_id")
            query = "SELECT * FROM Objednavka"
    elif choice_table == 6:
            print("ID | pobocka_id | zamestnanec_id")
            query = "SELECT * FROM prace"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


"""
Tento kód implementuje funkci pro zobrazování dat z tabulek v databázi. Vstupem je objekt typu mysql.connector.connection,
z něhož se vytvoří cursor. Poté se vytiskne nabídka tabulek, uživatel si vybere tabulku, 
pro kterou chce zobrazit data a podle výběru se sestaví dotaz SELECT * FROM tabulka. 
Dotaz se poté provede pomocí metody execute() a výsledek se uloží do proměnné result. Následně se funkce vrátí hodnota result.
"""
