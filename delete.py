

"""
Tento kód slouží k mazání dat z databáze. Uživatel si vybere tabulku, ze které chce smazat data, a poté zadá ID položky, kterou chce smazat.
Kód vyhodnotí, zda nejsou na danou položku v databázi nějaké vazby,
a pokud ano, vypíše chybové hlášení a ukončí funkci.
Pokud ne, provede DELETE příkaz a potvrdí úspěšné smazání.
"""
def delete_data(cnx):
    result = None
    cursor = cnx.cursor()
    print("==========TABULKY===========")
    print("1. Uzivatel")
    print("2. Produkt")
    print("3. Pobocka")
    print("4. Zamestnanec")
    print("5. Objednavka")
    print("6. Prace")
    print("============================")
    choice_table = int(input("Enter the number of the table you want to delete data from: "))
    if choice_table == 1:
        query = "DELETE FROM Uzivatel WHERE ID=%s"
        id = input("Enter the ID of the user you want to delete: ")
        check_query = "SELECT * FROM Objednavka WHERE uz_id=%s"
        cursor.execute(check_query, (id,))
        if cursor.fetchall():
            print("======================ERROR================================")
            print("You must delete the Objednavka with this Uzivatel ID first.")
            print("===========================================================")
            return
    elif choice_table == 2:
        query = "DELETE FROM Produkt WHERE ID=%s"
        id = input("Enter the ID of the product you want to delete: ")
        check_query = "SELECT * FROM Produkt WHERE prod_id=%s"
        cursor.execute(check_query, (id,))
        if cursor.fetchall():
            print("======================ERROR================================")
            print("You must delete the Objednavka with this Produkt ID first.")
            print("===========================================================")
        return
    elif choice_table == 3:
        query = "DELETE FROM Pobocka WHERE ID=%s"
        id = input("Enter the ID of the branch you want to delete: ")
        check_query = "SELECT * FROM prace WHERE pob_id=%s"
        check_query2 = "SELECT * FROM Objednavka WHERE pob_id=%s"
        cursor.execute(check_query, (id,))
        cursor.execute2(check_query2, (id,))
        if cursor.fetchall():
            print("======================ERROR================================")
            print("You must delete the Prace or Objednavka with this branch ID first.")
            print("===========================================================")
            return
    elif choice_table == 4:
        query = "DELETE FROM Zamestnanec WHERE ID=%s"
        id = input("Enter the ID of the employee you want to delete: ")
        check_query = "SELECT * FROM prace WHERE zam_id=%s"
        cursor.execute(check_query, (id,))
        if cursor.fetchall():
            print("======================ERROR================================")
            print("You must delete the Prace with this employee ID first.")
            print("===========================================================")
            return
    elif choice_table == 5:
        query = "DELETE FROM Objednavka WHERE ID=%s"
        id = input("Enter the ID of the order you want to delete: ")
    elif choice_table == 6:
        query = "DELETE FROM prace WHERE ID=%s"
        id = input("Enter the ID of the work you want to delete: ")
    cursor.execute(query, (id,))
    cnx.commit()
    print("Data deleted successfully.")