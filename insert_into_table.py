
"""
Tento kód slouží k vložení nového záznamu do jedné ze šesti tabulek (Uzivatel, Produkt, Pobocka, Zamestnanec, Objednavka, Prace).
Po spuštění se zobrazí nabídka pro výběr tabulky, do které se má vložit záznam.
Po výběru tabulky se uživatel ptá na hodnoty jednotlivých sloupců, které se poté vloží pomocí dotazu.
Po úspěšném vložení se zobrazí počet vložených záznamů (většinou 1).
"""

def insert_into_table(cnx):
    cursor = cnx.cursor()
    result = None
    print("==========TABULKY===========")
    print("1. Uzivatel")
    print("2. Produkt")
    print("3. Pobocka")
    print("4. Zamestnanec")
    print("5. Objednavka")
    print("6. Prace")
    print("============================")
    choice_table = int(input("Enter your choice: "))
    if choice_table == 1:
            table = "Uzivatel"
            Jmeno = input("Jmeno: ")
            Prijmeni = input("Prijmeni: ")
            Email = input("Email: ")
            Datum_nar = input("Datum narozeni (YYYY-MM-DD): ")
            values = (Jmeno, Prijmeni, Email, Datum_nar)
            query = "INSERT INTO Uzivatel (Jmeno, Prijmeni, Email, Datum_nar) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, values)
            cnx.commit()
            print(cursor.rowcount, "record inserted.")
    elif choice_table == 2:
            table = "Produkt"
            Nazev = input("Nazev: ")
            Rozmer = input("Rozmer (S,M,L,XL,XXL): ")
            Barva = input("Barva: ")
            Cena = float(input("Cena: "))
            Dostupnost = int(input("Dostupnost (True = 1 / False = 0): "))
            values = (Nazev, Rozmer, Barva, Cena, Dostupnost)
            query = "INSERT INTO Produkt (Nazev, Rozmer, Barva, Cena, Dostupnost) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, values)
            cnx.commit()
            print(cursor.rowcount, "record inserted.")
    elif choice_table == 3:
            table = "Pobocka"
            Adresa = input("Adresa: ")
            Cislo_popisne = int(input("Cislo_popisne: "))
            PSC = int(input("PSC: "))
            values = (Adresa, Cislo_popisne, PSC)
            query = "INSERT INTO Pobocka (Adresa, Cislo_popisne, PSC) VALUES (%s, %s, %s)"
            cursor.execute(query, values)
            cnx.commit()
            print(cursor.rowcount, "record inserted.")
    elif choice_table == 4:
            table = "Zamestnanec"
            Jmeno = input("Jmeno: ")
            Prijmeni = input("Prijmeni: ")
            Zacatek_prace = input("Enter Datum_nar (YYYY-MM-DD): ")
            values = (Jmeno, Prijmeni, Zacatek_prace)
            query = "INSERT INTO Zamestnanec (Jmeno, Prijmeni, Zacatek_prace) VALUES (%s, %s, %s)"
            cursor.execute(query, values)
            cnx.commit()
            print(cursor.rowcount, "record inserted.")
    elif choice_table == 5:
                table = "Objednavka"
                Datum_obj = input("Datum_obj: ")
                ID_uzivatele = int(input("ID_uzivatele: "))
                ID_pobocky = int(input("ID_pobocky: "))
                ID_produkt = int(input("ID_produktu: "))
                Prosla_platba = input("Prosla_platba: ")
                values = (Datum_obj, ID_uzivatele, ID_pobocky, ID_produkt, Prosla_platba)
                query = "INSERT INTO Objednavka (Datum_obj, ID_uzivatele, ID_pobocky, ID_produkt, Prosla_platba) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, values)
                cnx.commit()
                print(cursor.rowcount, "record inserted")
    elif choice_table == 6:
                table = "prace"
                query = "SELECT * FROM Pobocka"
                cursor.execute(query)
                result = cursor.fetchall()
                print("ID,Adresa")
                for row in result:
                    print(row)
                pod_id = input("Enter ID_pobocka ze seznamu vyse: ")
                query = "SELECT * FROM Zamestnanec"
                cursor.execute(query)
                result = cursor.fetchall()
                print("ID,Jmeno, Prijmeni")
                for row in result:
                    print(row)
                zam_id = input("Enter ID_zamestnance ze seznamu vyse: ")
                values = (pod_id, zam_id)
                query = "INSERT INTO prace (pod_id,zam_id ) VALUES (%s, %s)"
                cursor.execute(query, values)
                cnx.commit()
                print(cursor.rowcount, "record inserted.")
                return result
