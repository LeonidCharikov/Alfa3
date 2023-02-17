import sys
import mysql.connector
import display_options
import display_views
import display_table
import insert_into_table
import delete
import update_table
import import_data
from import_data import import_csv

"""
Funkce connection() se používá k připojení k databázi a vrátí objekt připojení.
"""
def connection():
    cnx = mysql.connector.connect(user='root',
                              host='localhost',
                              database='obchod')
    return cnx


"""
V souboru import_data.py se nachází funkce import_csv pro importování dat z CSV souboru do databáze. 
Ostatní soubory (display_options, display_views, display_table, insert_into_table, delete, update_table)
implementují operace jako zobrazování pohledů, tabulek, vkládání, mazání a aktualizace dat.
"""

"""
Funkce main() implementuje hlavní logiku programu a nabízí uživateli výběr z různých operací pomocí funkce display_options.options(). 
Podle výběru volí správnou funkci z ostatních souborů a vypíše výsledek. 
Program běží v nekonečné smyčce, dokud uživatel nezvolí možnost 8, kdy se ukončí.
"""


def main():
    cnx = connection()
    while True:
        choice = display_options.options()
        if choice == 1:
            table_result = display_views.display_view1(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 2:
            table_result = display_views.display_view2(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 3:
            table_result = display_table.display_table(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 4:
            table_result = insert_into_table.insert_into_table(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 5:
            table_result = delete.delete_data(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 6:
            table_result = update_table.update(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 7:
            table_result = import_data.import_csv(cnx)
            if table_result:
                for row in table_result:
                    print(row)
        elif choice == 8:
            cnx.close()
            sys.exit()
        else:
            print("Invalid option selected. Please choose again.")
            display_options.options()

if __name__ == "__main__":
    main()
