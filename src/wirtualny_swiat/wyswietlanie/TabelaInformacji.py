from tkinter import Label

class TabelaInformacji:
    MAKSYMALNA_ILOSC=20
    def __init__(self):
        self.__iloscKomunikatow = 0
        self.__komunikaty = []
    
    def dodajKomunikat(self, komunikat):
        if(self.__iloscKomunikatow == TabelaInformacji.MAKSYMALNA_ILOSC):
            self.__komunikaty.pop()
            self.__komunikaty.insert(0, Label(text=komunikat))
        else:
            self.__komunikaty.insert(0, Label(text=komunikat))
        
        for i in range(self.__iloscKomunikatow):
                self.__komunikaty.grid(row=i, column=21)
    
    def dodajRezultatWalki(self, wygrany, przegrany, numerTury):
        
        komunikat="Tura nr {nrTury} na polu: ({wygranyX},{wygranyY}) {typWygrany} zabija {typPrzegrany}.".format(
                    nrTury=numerTury, wygranyX=wygrany.aktualnePolozenie.x, wygranyY=wygrany.aktualnePolozenie.y,
                    typWygrany=wygrany.typJakoString(), typPrzegrany=przegrany.typJakoString())
        self.dodajKomunikat(komunikat=komunikat)
        
    def dodajRozmnazanie(self, wspolrzedneNowego, typ, numerTury):
        komunikat="Tura nr {nrTury} na polu ({nowyX},{nowy.Y}) urodzil sie nowy {typ}.".format(
                    nrTury=numerTury, nowyX=wspolrzedneNowego.x, nowyY=wspolrzedneNowego.y, typ=typ)
        self.dodajKomunikat(komunikat=komunikat)
        
    def dodajZjedzenie(self, zwierze, roslina, numerTury):
        komunikat="Tura nr {nrTury} na polu: ({wspX},{wspY}) {typZwierze} zjada {typRoslina}.".format(
                    nrTury=numerTury, wspX=zwierze.aktualnePolozenie.x, wspY=zwierze.aktualnePolozenie.y, 
                    typZwierze=zwierze.typJakoString(), typRoslina=roslina.typJakoString())
        self.dodajKomunikat(komunikat=komunikat)
    
    def dodajZasianie(self, wspolrzedne, typ, numerTury):
        komunikat = "Tura nr {nrTury} na polu ({wspX},{wspY}) wyrosla roslina: {typRosliny}.".format(
                    nrTury=numerTury, wspX=wspolrzedne.x, wspY=wspolrzedne.y, typRosliny=typ)
        self.dodajKomunikat(komunikat=komunikat)
    
    
    
    
    
