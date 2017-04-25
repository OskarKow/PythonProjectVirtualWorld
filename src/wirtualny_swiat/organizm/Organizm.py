from abc import ABCMeta, abstractmethod

class TYP_ORGANIZMU:
    ZOLW, CZLOWIEK, WILK, OWCA, ANTYLOPA, LIS, TRAWA, MLECZ, GUARANA, JAGODY, PUSTE = range(11)
    
class WPROWADZENIE:
    STRZ_GORA, STRZ_DOL, STRZ_LEWO, STRZ_PRAWO, UMIEJETNOSC = range(5)
    

class Organizm:
    __metaclass__ = ABCMeta
    _inicjatywa = 0
    _sila = 0
    _wiek = 0
    _aktualnePolozenie = None
    _poprzedniePolozenie = None
    _typ = None
    
    @abstractmethod
    def akcja(self, swiat): pass
    
    @abstractmethod
    def walcz(self, swiat, napastnik): pass
    
    @abstractmethod
    def typJakoString(self): pass
    
    @property
    def sila(self):
        return self._sila
    
    def zwiekszSile(self):
        self._sila = self._sila + 3
        
    @property
    def inicjatywa(self):
        return self._inicjatywa
    
    @property
    def wiek(self):
        return self._wiek
    
    def zwiekszWiek(self):
        self.__wiek = self._wiek + 1
        
    @property
    def aktualnePolozenie(self):
        return self._aktualnePolozenie
    
    @aktualnePolozenie.setter
    def aktualnePolozenie(self, nowe):
        self._aktualnePolozenie = nowe
    
    @property
    def poprzedniePolozenie(self):
        return self._poprzedniePolozenie
    
    @poprzedniePolozenie.setter
    def poprzedniePolozenie(self, nowe):
        self._poprzedniePolozenie = nowe
        
    @property
    def typ(self):
        return self._typ
    
    @staticmethod
    def stringToTyp(self, napis):
        if(napis == "Wilk"):
            return TYP_ORGANIZMU.WILK
        if(napis == "Zolw"):
            return TYP_ORGANIZMU.ZOLW
        if(napis == "Czlowiek"):
            return TYP_ORGANIZMU.Czlowiek
        if(napis == "Lis"):
            return TYP_ORGANIZMU.LIS
        if(napis == "Owca"):
            return TYP_ORGANIZMU.OWCA
        if(napis == "Antylopa"):
            return TYP_ORGANIZMU.ANTYLOPA
        if(napis == "Trawa"):
            return TYP_ORGANIZMU.TRAWA
        if(napis == "Guarana"):
            return TYP_ORGANIZMU.GUARANA
        if(napis == "Mlecz"):
            return TYP_ORGANIZMU.MLECZ
        if(napis == "Jagody"):
            return TYP_ORGANIZMU.JAGODY
