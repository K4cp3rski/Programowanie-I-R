class Menager_hasla:
    def __init__(self):
        pass
    stare_haslo = []

    def uzyskanie_hasla(self):
        if len(self.stare_haslo) != 0:
            haslo = self.stare_haslo.pop()
            self.stare_haslo.append(haslo)
            return haslo
        else:
            return "Null"

    def ustawianie_hasla(self, nowe):
        # haslo = Menager_hasla.uzyskanie_hasla(self)
        if nowe not in Menager_hasla.stare_haslo:
            Menager_hasla.stare_haslo.append(nowe)
            print("Hasło zostało zmienione")
        else:
            print("To hasło już zostało zajęte")

    def jest_poprawne(self, test):
        haslo = self.uzyskanie_hasla()
        if test == haslo:
            return True
        else:
            return False


Menager = Menager_hasla()
Menager.stare_haslo.append("Ala")
Menager.stare_haslo.append("Kacper")
print("Obecne hasło to:", Menager.uzyskanie_hasla())
Menager.ustawianie_hasla("Ola")
print(Menager.jest_poprawne("Kacper"))
print(Menager.jest_poprawne("Ola"))
# print(Menager.stare_haslo)
