from wirtualny_swiat.Point import Point
from wirtualny_swiat.organizm.KontenerOrganizmow import KontenerOrganizmow
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.organizm.zwierzeta import *
from wirtualny_swiat.organizm.rosliny import *
from wirtualny_swiat.organizm.zwierzeta.Wilk import Wilk
from wirtualny_swiat.organizm.zwierzeta.Zolw import Zolw
from wirtualny_swiat.organizm.zwierzeta.Lis import Lis
from wirtualny_swiat.organizm.zwierzeta.Czlowiek import Czlowiek
from wirtualny_swiat.organizm.zwierzeta.Antylopa import Antylopa
from wirtualny_swiat.organizm.zwierzeta.Owca import Owca
from wirtualny_swiat.organizm.rosliny.Trawa import Trawa
from wirtualny_swiat.organizm.rosliny.Mlecz import Mlecz
from wirtualny_swiat.organizm.rosliny.Guarana import Guarana
from wirtualny_swiat.organizm.rosliny.Jagody import Jagody
from tkinter import Label
import random

class Swiat:
    def __init__(self, okno):
        self.__okno = okno
        self.__kontener = KontenerOrganizmow()
        self.__doDodania = KontenerOrganizmow()
        self.__doUsuniecia = KontenerOrganizmow()
        self.__numerTury = 0
        self.__oknoProgramu = okno
        self.__generatorLosowych = random.Random()
        self.__aktualneWprowadzenie = 0
        self.__plansza = []
        #USTAWIENIE PLANSZY
        for i in range(20):
            for j in range(20):
                self.__plansza.append(TYP_ORGANIZMU.PUSTE)
        typy = (TYP_ORGANIZMU.WILK, TYP_ORGANIZMU.ZOLW, TYP_ORGANIZMU.ANTYLOPA, TYP_ORGANIZMU.LIS, TYP_ORGANIZMU.OWCA,
                     TYP_ORGANIZMU.TRAWA, TYP_ORGANIZMU.MLECZ, TYP_ORGANIZMU.GUARANA, TYP_ORGANIZMU.JAGODY, TYP_ORGANIZMU.CZLOWIEK)
        wspolrzedne = []
        powtarzaSie = False
        for i in range(19):
            while(True):
                randX = self.__generatorLosowych.randrange(20)
                randY = self.__generatorLosowych.randrange(20)
                wspolrzedne.append(Point(randX, randY))
                for j in range(i):
                    if(wspolrzedne[-1].x == wspolrzedne[j].x and wspolrzedne[-1].y == wspolrzedne[j].y):
                        powtarzaSie = True
                        wspolrzedne.pop()
                        break
                if(powtarzaSie == False): break
            self.__doDodania.dodajOrganizm(self.stworzOrganizm(wspolrzedne[-1], typy[i // 2]))
        self.przepiszDoDodania()
        self.aktualizujPlansze()
    
    def przepiszDoDodania(self):
        for org in self.__doDodania.organizmy:
            currentCoord = org.aktualnePolozenie
            self.__kontener.dodajOrganizm(org)
            self.setPole(currentCoord, org.typ)
        self.__doDodania.wyczysc()
    
    def aktualizujPlansze(self):
        for i in range(20):
            for j in range(20):
                self.__oknoProgramu.setIkona(j, i, TYP_ORGANIZMU.PUSTE)
        
        for org in self.__kontener.organizmy:
            self.__oknoProgramu.setIkona(org.aktualnePolozenie.x, org.aktualnePolozenie.y, org.typ)
        
    def getPole(self, pole):
        return self.__plansza[20 * pole.y + pole.x]
    
    def setPole(self, pole, typ):
        self.__plansza[20 * pole.y + pole.x] = typ
        
    def getOrganizm(self, wspolrzedne):
        for org in self.__kontener.organizmy:
            if(org.aktualnePolozenie.x == wspolrzedne.x and org.aktualnePolozenie.y == wspolrzedne.y 
               and self.__doUsuniecia.czyZawiera(org) == False):
                return org
        return None
    
    def getOrganizmPominiecie(self, wspolrzedne, do_pominiecia):
        for org in self.__kontener.organizmy:
            if(org is do_pominiecia):
                continue
            if(org.aktualnePolozenie.x == wspolrzedne.x and org.aktualnePolozenie.y == wspolrzedne.y
                and self.__doUsuniecia.czyZawiera(org) == False):
                return org
        return None
    
    @property
    def kontener(self):
        return self.__kontener
    
    @property
    def doDodania(self):
        return self.__doDodania
    
    @property
    def numerTury(self):
        return self.__numerTury
    
    @property
    def doUsuniecia(self):
        return self.__doUsuniecia
    @property
    def generatorLosowych(self):
        return self.__generatorLosowych
    
    @property
    def oknoProgramu(self):
        return self.__oknoProgramu
    
    @property
    def aktualneWprowadzenie(self):
        return self.__aktualneWprowadzenie
    
    @property
    def plansza(self):
        return self.__plansza
    
    @aktualneWprowadzenie.setter
    def aktualneWprowadzenie(self, nowe):
        self.__aktualneWprowadzenie = nowe
    @kontener.setter
    def kontener(self, nowy):
        self.__kontener = nowy
    @doDodania.setter
    def doDodania(self, nowy):
        self.__doDodania = nowy
    @doUsuniecia.setter
    def doUsuniecia(self, nowy):
        self.__doUsuniecia = nowy
    @numerTury.setter
    def numerTury(self, nowy):
        self.__numerTury = nowy
    @plansza.setter
    def plansza(self, nowa):
        self.__plansza = nowa
    
    def wylosujWolnePole(self,centralne):
        wolne = []
        
        if(centralne.y > 0 and self.__plansza[20*(centralne.y - 1) + centralne.x] == TYP_ORGANIZMU.PUSTE):
            wolne.append(Point(x=centralne.x, y=centralne.y - 1))
        if(centralne.x < 19 and self.__plansza[20*centralne.y + centralne.x + 1] == TYP_ORGANIZMU.PUSTE):
            wolne.append(Point(x=centralne.x + 1, y=centralne.y))
        if(centralne.y < 19 and self.__plansza[20*(centralne.y + 1) + centralne.x] == TYP_ORGANIZMU.PUSTE):
            wolne.append(Point(x=centralne.x, y=centralne.y + 1))
        if(centralne.x > 0 and self.__plansza[20*centralne.y + centralne.x - 1] == TYP_ORGANIZMU.PUSTE):
            wolne.append(Point(x=centralne.x - 1, y=centralne.y))
        
        if(len(wolne) == 0):
            return Point(-1, -1)
        indeks = self.__generatorLosowych.randrange(0, len(wolne))
        return wolne[indeks]
    
    def stworzOrganizm(self, pole, typ):
        if(typ == TYP_ORGANIZMU.WILK):
            return Wilk(pole)
        if(typ == TYP_ORGANIZMU.ZOLW):
            return Zolw(pole)
        if(typ == TYP_ORGANIZMU.LIS):
            return Lis(pole)
        if(typ == TYP_ORGANIZMU.ANTYLOPA):
            return Antylopa(pole)
        if(typ == TYP_ORGANIZMU.OWCA):
            return Owca(pole)
        if(typ == TYP_ORGANIZMU.CZLOWIEK):
            return Czlowiek(pole)
        if(typ == TYP_ORGANIZMU.TRAWA):
            return Trawa(pole)
        if(typ == TYP_ORGANIZMU.MLECZ):
            return Mlecz(pole)
        if(typ == TYP_ORGANIZMU.GUARANA):
            return Guarana(pole)
        if(typ == TYP_ORGANIZMU.JAGODY):
            return Jagody(pole)
    
    def wykonajTure(self):
        self.__numerTury = self.__numerTury + 1
        for org in self.__kontener.organizmy:
            if(self.__doUsuniecia.czyZawiera(org) == False):
                org.zwiekszWiek()
                org.akcja(self)
        self.przepiszDoDodania()
        self.usunDoUsuniecia()
        self.aktualizujPlansze()
    
    def usunDoUsuniecia(self):
        for org in self.__doUsuniecia.organizmy:
            self.__kontener.usunOrganizm(org)
        self.__doUsuniecia.wyczysc()
        