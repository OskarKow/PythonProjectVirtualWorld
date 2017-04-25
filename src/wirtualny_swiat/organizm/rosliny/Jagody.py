from wirtualny_swiat.organizm.rosliny.Roslina import Roslina
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.Point import Point

class Jagody(Roslina):
    def __init__(self, aktualne, poprzednie=None, sila=None, wiek=None):
        self._typ = TYP_ORGANIZMU.JAGODY
        self._aktualnePolozenie = aktualne
        self._inicjatywa = 0
        if(poprzednie is None and sila is None and wiek is None):
            self._sila = 99
            self._wiek = 0
            self._poprzedniePolozenie = aktualne
        else:
            self._sila = sila
            self._wiek = wiek
            self._poprzedniePolozenie = poprzednie
    
    def akcja(self, swiat):
        losowa = swiat.generatorLosowych.randrange(100 // Roslina.SZANSA_ZASIANIA)
        if(losowa == 0):
            self.rozprzestrzeniajSie(swiat)
    
    def walcz(self, swiat, napastnik):
        swiat.setPole(napastnik.poprzedniePolozenie, TYP_ORGANIZMU.PUSTE)
        swiat.doUsuniecia.dodajOrganizm(napastnik)
        swiat.doUsuniecia.dodajOrganizm(self)
        swiat.setPole(self._aktualnePolozenie, TYP_ORGANIZMU.PUSTE)
        swiat.oknoProgramu.dodajZjedzenie(napastnik, self, swiat.numerTury)
    
    def typJakoString(self):
        return "Jagody"        