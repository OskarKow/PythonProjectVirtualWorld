from wirtualny_swiat.organizm.zwierzeta.Zwierze import Zwierze
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.organizm.Organizm import WPROWADZENIE
from wirtualny_swiat.Point import Point

class Czlowiek(Zwierze):
    def __init__(self, aktualne, poprzednie=None, sila=None, wiek=None):
        self._typ = TYP_ORGANIZMU.CZLOWIEK
        self._aktualnePolozenie = aktualne
        self._inicjatywa = 8
        self._pozostalyCooldown = 0
        if(poprzednie is None and sila is None and wiek is None):
            self._sila = 5
            self._wiek = 0
            self._poprzedniePolozenie = aktualne
        else:
            self._sila = sila
            self._wiek = wiek
            self._poprzedniePolozenie = poprzednie
    
    def poprawneWprowadzenie(self, swiat):
        wpr = swiat.aktualneWprowadzenie
        if(wpr == WPROWADZENIE.UMIEJETNOSC and self._pozostalyCooldown > 0):
            return False
        elif(wpr == WPROWADZENIE.STRZ_DOL and self._aktualnePolozenie.y >= 19):
            return False
        elif(wpr == WPROWADZENIE.STRZ_GORA and self._aktualnePolozenie.y <= 0):
            return False
        elif(wpr == WPROWADZENIE.STRZ_LEWO and self._aktualnePolozenie.x <= 0):
            return False
        elif(wpr == WPROWADZENIE.STRZ_PRAWO and self._aktualnePolozenie.x >= 19):
            return False
        return True
    
    def typJakoString(self):
        return "Czlowiek"
    
    def akcja(self, swiat):
        if(self._pozostalyCooldown > 0):
            self._pozostalyCooldown = self._pozostalyCooldown - 1
        if(self.poprawneWprowadzenie(swiat) == True):
            wpr = swiat.aktualneWprowadzenie
            if(wpr == WPROWADZENIE.UMIEJETNOSC):
                self.umiejetnosc(swiat)
            elif(wpr == WPROWADZENIE.STRZ_DOL):
                self.poruszSie(swiat, Point(self._aktualnePolozenie.x, self._aktualnePolozenie.y + 1))
            elif(wpr == WPROWADZENIE.STRZ_GORA):
                self.poruszSie(swiat, Point(self._aktualnePolozenie.x, self._aktualnePolozenie.y - 1))
            elif(wpr == WPROWADZENIE.STRZ_LEWO):
                self.poruszSie(swiat, Point(self._aktualnePolozenie.x - 1, self._aktualnePolozenie.y))
            elif(wpr == WPROWADZENIE.STRZ_PRAWO):
                self.poruszSie(swiat, Point(self._aktualnePolozenie.x + 1, self._aktualnePolozenie.y))
    
    def kolizja(self, swiat):
        drugi = swiat.getOrganizmPominiecie(self._aktualnePolozenie, self)
        if(drugi is None):
            pass
        else:
            if(drugi.typ == self._typ):
                self.rozmnazajSie(swiat)
            else:
                drugi.walcz(swiat, self)
    
    def umiejetnosc(self, swiat):
        self._pozostalyCooldown = 5
        sasiednie = []
        sasiednie.append(Point(self._aktualnePolozenie.x - 1, self._aktualnePolozenie.y - 1))
        sasiednie.append(Point(self._aktualnePolozenie.x, self._aktualnePolozenie.y - 1))
        sasiednie.append(Point(self._aktualnePolozenie.x + 1, self._aktualnePolozenie.y - 1))
        sasiednie.append(Point(self._aktualnePolozenie.x + 1, self._aktualnePolozenie.y))
        sasiednie.append(Point(self._aktualnePolozenie.x + 1, self._aktualnePolozenie.y + 1))
        sasiednie.append(Point(self._aktualnePolozenie.x, self._aktualnePolozenie.y + 1))
        sasiednie.append(Point(self._aktualnePolozenie.x - 1, self._aktualnePolozenie.y + 1))
        sasiednie.append(Point(self._aktualnePolozenie.x - 1, self._aktualnePolozenie.y))
        for pole in sasiednie:
            if(pole.x >=0 and pole.x <= 19 and pole.y >= 0 and pole.y <= 19):
                doZniszczenia = swiat.getOrganizm(pole)
                if(not(doZniszczenia is None)):
                    swiat.doUsuniecia.dodajOrganizm(doZniszczenia)
                    swiat.setPole(pole, TYP_ORGANIZMU.PUSTE)
        