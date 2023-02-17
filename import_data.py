import mysql.connector


"""
Soubor se načte a pro každý řádek se v databázi kontroluje, 
zda data již neexistují. Pokud existují, funkce vypíše chybovou hlášku. Pokud neexistují, data se vloží do tabulky.

Pokud dojde k chybě při importu dat, funkce provede vrácení změn v databázi pomocí metody rollback(). 
Pokud je import úspěšný, funkce provede commit() změn do databáze.
"""

def import_csv(cnx):
    cursor = cnx.cursor()
    print("==========TABULKY===========")
    print("1. Uzivatel")
    print("2. Produkt")
    print("============================")
    table_choice = int(input('Enter the table number to import data: '))
    table_map = {
        1: ('Uzivatel', 'ID,Jmeno,Prijmeni,Email,Datum_nar'),
        2: ('Produkt', 'ID,Nazev,Barva,Rozmer,Cena,Dostupnost')
    }

    if table_choice not in table_map:
        print('Invalid table choice')
        return

    table_name, columns = table_map[table_choice]
    file_name = input("Enter the file name (including the extension, e.g. .csv): ")
    file_path = input("Enter the file path (e.g. C:\data + file name): ")
    try:
        with open(file_path + file_name) as file:
            for line in file:
                values = line.strip().split(',')
                query = f'SELECT {columns} FROM {table_name} WHERE {columns} = {tuple(values)}'
                cursor.execute(query)
                result = cursor.fetchone()

                if result:
                    print(f'Error: Data {values} already exists in the {table_name} table.')
                    return
                else:
                    query = f'INSERT INTO {table_name} ({columns}) VALUES {tuple(values)}'
                    cursor.execute(query)

        cnx.commit()
        print(f'Data imported into {table_name} successfully')
    except FileNotFoundError:
        print(f'File {file_name} not found')
    except mysql.connector.IntegrityError as error:
        cnx.rollback()
        print(f'Error: {error}')





