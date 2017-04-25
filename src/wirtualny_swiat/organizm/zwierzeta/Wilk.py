from wirtualny_swiat.organizm.zwierzeta.Zwierze import Zwierze
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.Point import Point

class Wilk(Zwierze):
    def __init__(self, aktualne, poprzednie=None, sila=None, wiek=None):
        self._typ = TYP_ORGANIZMU.WILK
        self._aktualnePolozenie = aktualne
        self._inicjatywa = 5
        if(poprzednie is None and sila is None and wiek is None):
            self._sila = 9
            self._wiek = 0
            self._poprzedniePolozenie = aktualne
        else:
            self._sila = sila
            self._wiek = wiek
            self._poprzedniePolozenie = poprzednie
    
    def akcja(self, swiat):
        nowe_pole = self.wylosujSasiedniePole()
        self.poruszSie(swiat, nowe_pole)
        
    def kolizja(self, swiat):
        drugi = swiat.getOrganizmPominiecie(self._aktualnePolozenie, self)
        if(drugi is None):
            pass
        else:
            if(drugi.typ == self._typ):
                self.rozmnazajSie(swiat)
            else:
                drugi.walcz(swiat, self)
    
    def typJakoString(self):
        return "Wilk"
                
    