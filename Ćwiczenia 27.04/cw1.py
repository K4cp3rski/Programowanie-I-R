class Rabat:
    magazyn = {}

    def dostawa(self, nazwa, ilosc, cena):
        self.magazyn[nazwa] = [ilosc, cena]

    def uzyskanie_ceny(self, nazwa, ilosc):
        cena_bazowa = self.magazyn[nazwa][1]
        cena = 0
        if ilosc < 10:
            cena = ilosc * cena_bazowa
        elif ilosc < 100:
            cena = ilosc * 0.95 * cena_bazowa
        else:
            cena = ilosc * 0.9 * cena_bazowa
        return cena
    def dokonanie_zakupu(self, nazwa, ilosc):
        ilosc_bazowa = self.magazyn[nazwa][0]
        if ilosc > ilosc_bazowa:
            return "Nie ma tyle produktów na stanie"
        else:
            cena = self.uzyskanie_ceny(nazwa, ilosc)
            self.magazyn[nazwa][0] -= ilosc
            return fr"Kupiono {ilosc} produktów '{nazwa}' za cenę {cena} zł"
R1 = Rabat()
R1.dostawa('Truskawka', 100, 1)
R1.dostawa('Banan', 20, 3)
print("Stan magazynu:")
print(R1.magazyn, "\n")
print(fr"Cena 200 truskawek to {R1.uzyskanie_ceny('Truskawka', 200)} zł")
print(R1.dokonanie_zakupu('Truskawka', 20))
print(R1.dokonanie_zakupu('Truskawka', 90))
print("\nStan magazynu:")
print(R1.magazyn)



