from wirtualny_swiat.organizm.zwierzeta.Zwierze import Zwierze
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.Point import Point

class Antylopa(Zwierze):
    def __init__(self, aktualne, poprzednie=None, sila=None, wiek=None):
        self._typ = TYP_ORGANIZMU.ANTYLOPA
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
    
    def walcz(self, swiat, napastnik):
        ucieczka = swiat.generatorLosowych.randrange(1)
        
        if(ucieczka == 0):
            nowe_pole = swiat.wylosujWolnePole(self._aktualnePolozenie)
            if(nowe_pole.x >= 0 and nowe_pole.y >= 0):
                swiat.setPole(napastnik.aktualnePolozenie, napastnik.typ)
                swiat.setPole(napastnik.poprzedniePolozenie, TYP_ORGANIZMU.PUSTE)
                self._poprzedniePolozenie = self._aktualnePolozenie
                self._aktualnePolozenie = nowe_pole
                swiat.setPole(self._aktualnePolozenie, self._typ)
            else:
                super().walcz(swiat, self)
    
    def akcja(self, swiat):
        mozliwePola = []
        if(self._aktualnePolozenie.y > 1):
            mozliwePola.append(Point(self._aktualnePolozenie.x, self._aktualnePolozenie.y - 2))
        if (self._aktualnePolozenie.x < 18):
            mozliwePola.append(Point(self._aktualnePolozenie.x + 2, self._aktualnePolozenie.y))
        if(self._aktualnePolozenie.y < 18):
            mozliwePola.append(Point(self._aktualnePolozenie.x, self._aktualnePolozenie.y + 2))
        if(self._aktualnePolozenie.x > 1):
            mozliwePola.append(Point(self._aktualnePolozenie.x - 2, self._aktualnePolozenie.y))
        
        losowa = swiat.generatorLosowych.randrange(len(mozliwePola))
        self.poruszSie(swiat, mozliwePola[losowa])
    
    def kolizja(self, swiat):
        drugi = swiat.getOrganizmPominiecie(self._aktualnePolozenie, self)
        if(drugi is None):
            print("none a nie powinno")
        else:
            if(drugi.typ == self._typ):
                self.rozmnazajSie(swiat)
            else:
                drugi.walcz(swiat, self)
    
    def typJakoString(self):
        return "Antylopa"