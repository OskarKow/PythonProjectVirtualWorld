from wirtualny_swiat.organizm.Organizm import *
from abc import ABCMeta, abstractmethod
import random
from wirtualny_swiat.Point import Point

class Zwierze(Organizm):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def kolizja(self, swiat): pass
    
    def wylosujSasiedniePole(self):
        generator = random.Random()
        nowe = Point(0,0)
        
        while True:
            losowa = generator.randrange(0, 4)
            if(losowa == 0):
                nowe.set(x=self._aktualnePolozenie.x, y=self._aktualnePolozenie.y-1)
            elif(losowa == 1):
                nowe.set(x=self._aktualnePolozenie.x+1, y=self._aktualnePolozenie.y)
            elif(losowa == 2):
                nowe.set(x=self._aktualnePolozenie.x, y=self._aktualnePolozenie.y+1)
            elif(losowa == 3):
                nowe.set(x=self._aktualnePolozenie.x-1, y=self._aktualnePolozenie.y)
                
            if(nowe.x >= 0 and nowe.x <= 19 and nowe.y >= 0 and nowe.y <= 19):
                break;
        
        return nowe
    
    def poruszSie(self, swiat, docelowe):
        self._poprzedniePolozenie = self._aktualnePolozenie
        self._aktualnePolozenie = docelowe
        if(swiat.getPole(docelowe) == TYP_ORGANIZMU.PUSTE):
            swiat.setPole(pole=self._poprzedniePolozenie, typ=TYP_ORGANIZMU.PUSTE)
            swiat.setPole(pole=self._aktualnePolozenie, typ=self._typ)
        else:
            self.kolizja(swiat)
    
    def rozmnazajSie(self, swiat):
        self._aktualnePolozenie = self._poprzedniePolozenie
        wspolrzedne = swiat.wylosujWolnePole(self._aktualnePolozenie)
        
        if(wspolrzedne.x >= 0 and wspolrzedne.y >=0):
            swiat.doDodania.dodajOrganizm(swiat.stworzOrganizm(wspolrzedne, self._typ))
            swiat.oknoProgramu.dodajRozmnazanie(wspolrzedne, self.typJakoString(), swiat.numerTury)
    
    def walcz(self, swiat, napastnik):
        if(self.wygranaWalka(napastnik=napastnik)):
            swiat.doUsuniecia.dodajOrganizm(napastnik)
            swiat.setPole(pole=napastnik.poprzedniePolozenie, typ=TYP_ORGANIZMU.PUSTE)
            swiat.oknoProgramu.dodajRezultatWalki(wygrany=self, przegrany=napastnik, numerTury=swiat.numerTury)
        else:
            swiat.doUsuniecia.dodajOrganizm(self)
            swiat.setPole(pole=self._aktualnePolozenie, typ=self._typ)
            swiat.setPole(pole=napastnik.poprzedniePolozenie, typ=TYP_ORGANIZMU.PUSTE)
            swiat.oknoProgramu.dodajRezultatWalki(wygrany=napastnik, przegrany=self, numerTury=swiat.numerTury)
        
    def wygranaWalka(self, napastnik):
        if(self._sila > napastnik.sila):
            return True
        else:
            return False
