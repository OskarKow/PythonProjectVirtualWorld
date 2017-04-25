from wirtualny_swiat.organizm.zwierzeta.Zwierze import Zwierze
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.Point import Point

class Zolw(Zwierze):
    def __init__(self, aktualne, poprzednie=None, sila=None, wiek=None):
        self._typ = TYP_ORGANIZMU.ZOLW
        self._aktualnePolozenie = aktualne
        self._inicjatywa = 1
        if(poprzednie is None and sila is None and wiek is None):
            self._sila = 2
            self._wiek = 0
            self._poprzedniePolozenie = aktualne
        else:
            self._sila = sila
            self._wiek = wiek
            self._poprzedniePolozenie = poprzednie
    
    def walcz(self, swiat, napastnik):
        if(napastnik.sila < 5):
            napastnik.aktualnePolozenie = napastnik.poprzedniePolozenie
        else:
            super().walcz(swiat, napastnik)# Czy to zadziala?
    
    def akcja(self, swiat):
        generator = swiat.generatorLosowych
        losowa = generator.randrange(4)
        if(losowa == 0):
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
        return "Zolw"
    
    
    
    
