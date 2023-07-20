class Pojisteny:
    """
    Definice tridy pro pojisteneho
    """
    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor tridy
        :param jmeno: zadava jmeno
        :param prijmeni: zadava prijmeni
        :param vek: zadava vek
        :param telefon: zadava telefon
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def to_string(self):
        """
        vraci textovy popis objektu
        :return:
        """
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"

    def vytvoreni_pojisteneho():
        """
        vytvoreni noveho pojistence
        :return:
        """
        pass
