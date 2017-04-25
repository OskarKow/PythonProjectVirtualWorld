from wirtualny_swiat.organizm.rosliny.Roslina import Roslina
from wirtualny_swiat.organizm.Organizm import *
from wirtualny_swiat.Point import Point

class Mlecz(Roslina):
    def __init__(self, aktualne, poprzednie=None, sila=None, wiek=None):
        self._typ = TYP_ORGANIZMU.MLECZ
        self._aktualnePolozenie = aktualne
        self._inicjatywa = 0
        if(poprzednie is None and sila is None and wiek is None):
            self._sila = 0
            self._wiek = 0
            self._poprzedniePolozenie = aktualne
        else:
            self._sila = sila
            self._wiek = wiek
            self._poprzedniePolozenie = poprzednie
    
    def akcja(self, swiat):
        probaUdana = False
        for i in range(3):
            losowa = swiat.generatorLosowych.randrange(100 // Roslina.SZANSA_ZASIANIA)
            if(losowa == 0):
                probaUdana = True
        if(probaUdana == True):
            self.rozprzestrzeniajSie(swiat)
    
    def typJakoString(self):
        return "Mlecz"
        
        
        
        
        
        
