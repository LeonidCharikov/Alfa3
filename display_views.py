

def display_view1(cnx):
    cursor = cnx.cursor()
    result = None
    query = "SELECT * FROM prehled_objednavky"
    cursor.execute(query)
    result = cursor.fetchall()
    print("===========================================Prehled Objednavky==============================================================")
    print("Datum objednavky | Nazev | Rozmer | Barva | Cena | Leonid | Charikov | Email | Prosla platba | Adresa | Cislo popisne | PSC")
    print("Datum_obj, Nazev, Rozmer, Barva, Cena, Jmeno, Prijmeni, Email, Prosla_platba, Adresa, Cislo_popisne, PSC")
    print("===========================================================================================================================")
    for row in result:
        print(row)
    return result

"""
Tento kód implementuje dva funkce, které se používají k výpisu dat z databáze. 
Funkce "display_view1" výpisuje všechny řádky z tabulky "prehled_objednavky" a "display_view2" výpisuje všechny řádky z tabulky "objednavky_uzivatel". 
Pro každou funkci se vytvoří kurzor a provede se dotaz na databázi, který je uložen v proměnné "query". Výsledek dotazu se uloží do proměnné "result". 
Poté se vypíšou hlavičky tabulky a řádky samotné. Výsledek se nakonec vrátí z funkce.
"""

def display_view2(cnx):
    cursor = cnx.cursor()
    result = None
    query = "SELECT * FROM objednavky_uzivatel"
    cursor.execute(query)
    result = cursor.fetchall()
    print("===================Objednavky Uzivatel====================")
    print("ID | Jmeno | Prijmeni | Email | Pocet objednavek")
    print("ID, Jmeno, Prijmeni, Email, Pocet_objednavek")
    print("==========================================================")
    for row in result:
         print(row)
    return result

