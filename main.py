import mysql.connector
from pojisteny import Pojisteny

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'projekt_database'
}

def create_pojisteni_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    """
    overeni jestli tabulka existuje nebo ne
    """
    cursor.execute("SHOW TABLES LIKE 'pojisteni'")
    table_exists = cursor.fetchone()

    if not table_exists:

        """
        vytvoreni tabulky v MYSQL
        """
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pojisteni (
                id INT AUTO_INCREMENT PRIMARY KEY,
                jmeno VARCHAR(50) NOT NULL,
                prijmeni VARCHAR(50) NOT NULL,
                vek INT NOT NULL,
                telefon VARCHAR(20) NOT NULL
            )
        ''')

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_pojisteni_table()


"""
ze souboru pojisteny.py importujeme tridu pojisteny
"""

def vytvoreni_pojisteneho():
    """
    vytvarime noveho pojisteneho
    :return: novy zaznam o pojistenem
    """
    jmeno = input("Zadejte jmeno pojisteneho:")
    prijmeni = input("Zadejte prijmeni pojisteneho:")
    vek = input("Zadejte vek pojisteneho:")
    telefon = input("Zadejte telefon pojisteneho:")
    pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
    return pojisteny

    """
    vytvoreni instance se zadanymi udaji
    """

def vypis_pojisteneho(seznam_pojisteny):
    """
    vypis informaci o pojistenych
    :param pojisteny:
    :return:
    """
    print("---------------------------------")
    print("Seznam pojistencu")
    print("---------------------------------")
    if seznam_pojisteny:
        for pojisteny in seznam_pojisteny:
            print(pojisteny.to_string())
            """
            slouzi k vypisu informaci o pojistenem
            
            """
    else:
        print("Neni ulozeny zadny zaznam")
    print("---------------------------------")

def najdi_pojisteneho(seznam_pojisteny, jmeno, prijmeni):
    """
    vyhledavani podle jmena a prijmeni
    """
    for pojisteny in seznam_pojisteny:
        if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
            return pojisteny
    return None

    """
    interakce uzivatele
    """
print("-------------------------------------")
print("Evidence pojistenych")
print("-------------------------------------")

seznam_pojisteny  = []
"""
seznam ze zacatku programu
"""
while True:
    print("Vyberte si akci:")
    print("1 - Pridat noveho pojisteneho")
    print("2 - Vypsat vsechny pojistene")
    print("3 - Vyhledat pojisteneho")
    print("4 - Konec")

    volba = input()

    if volba == "1":
        """
        pridavani noveho pojisteneho
        """
        pojisteny = vytvoreni_pojisteneho()
        """
        pripojeni dalsiho pojisteneho na konec seznamu
        """
        seznam_pojisteny.append(pojisteny)
        """
        ulozeni noveho pojisteneho do databaze 
        """
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute('''
                        INSERT INTO pojisteni (jmeno, prijmeni, vek, telefon)
                        VALUES (%s, %s, %s, %s)
                    ''', (pojisteny.jmeno, pojisteny.prijmeni, pojisteny.vek, pojisteny.telefon))
        conn.commit()
        cursor.close()
        conn.close()

        print("Data ulozena")
        """
        vypsani pojistenych
        """
    elif volba == "2":
        """
        vypsani seznamu zadanych pojistencu
        """
        if seznam_pojisteny:
            vypis_pojisteneho(seznam_pojisteny)
        else:
            print("Neni vlozen zadny pojisteny")
    elif volba == "3":
        """
        vyhledavani pojisteneho
        """
        jmeno = input("Zadejte jmeno pojisteneho pro vyhledavani: ")
        prijmeni = input("Zadejte prijmeni pojisteneho pro vyhledavani: ")
        nalezeny_pojisteny = najdi_pojisteneho(seznam_pojisteny, jmeno, prijmeni)
        if nalezeny_pojisteny:
            print("Nalezeny pojisteny:")
            print(nalezeny_pojisteny.to_string())
        else:
            print("Zaznam nenalezen")

    elif volba == "4":
        """
        ukonceni programu
        """
        break
    else:
        """
        neplatna volba, zadejte volbu znovu
        """
        print("Neplatna volba, zadejte volbu znovu")

    """
    zobrazeni vyzvy pokracujte libovolnou klavesou
    """
    input("Pokracujte libovolnou klavesou")
