from wirtualny_swiat.organizm.Organizm import *
from abc import ABCMeta, abstractmethod
from wirtualny_swiat.Point import Point

class Roslina(Organizm):
    __metaclass__ = ABCMeta
    SZANSA_ZASIANIA = 2
    
    def rozprzestrzeniajSie(self, swiat):
        wolne = swiat.wylosujWolnePole(self._aktualnePolozenie)
        if(wolne.x > -1 and wolne.y > -1):
            swiat.doDodania.dodajOrganizm(swiat.stworzOrganizm(wolne, self._typ))
            swiat.oknoProgramu.dodajZasianie(wolne, self.typJakoString(), swiat.numerTury)
    
    def walcz(self, swiat, napastnik):
        swiat.doUsuniecia.dodajOrganizm(self)
        swiat.setPole(self._aktualnePolozenie, napastnik.typ)
        swiat.setPole(napastnik.poprzedniePolozenie, TYP_ORGANIZMU.PUSTE)
        swiat.oknoProgramu.dodajZjedzenie(napastnik, self, swiat.numerTury)