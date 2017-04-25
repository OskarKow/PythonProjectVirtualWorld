from tkinter import *
from wirtualny_swiat.organizm.Organizm import TYP_ORGANIZMU
from wirtualny_swiat.organizm.Organizm import WPROWADZENIE
from wirtualny_swiat.swiat.Swiat import Swiat
import pickle

class OknoProgramu(Frame):
    MAX_KOMUNIKATOW = 20
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.__iloscKomunikatow=0
        self.__komunikaty=[]
        self.__tresciKomunikatow = []
        #ikony organizmow
        self.__owca = PhotoImage(file="sheep.gif")
        self.__lis = PhotoImage(file="fox.gif")
        self.__czlowiek = PhotoImage(file="human.gif")
        self.__wilk = PhotoImage(file="wolf.gif")
        self.__zolw = PhotoImage(file="turtle.gif")
        self.__antylopa = PhotoImage(file="antelope.gif")
        self.__trawa = PhotoImage(file="bush.gif")
        self.__mlecz = PhotoImage(file="mlecz.gif")
        self.__guarana = PhotoImage(file="guarana.gif")
        self.__jagody = PhotoImage(file="berries.gif")
        self.__puste = PhotoImage(file="puste.gif")
        self.__obrazki = []
        for i in range(20):
            for j in range(20):
                self.__obrazki.append(Label(image=None))
                self.__obrazki[-1].image=None
                self.__obrazki[-1].grid(row=i, column=j)
        
        self.__zapisz = Button(text="Zapisz", command=self.zapisz)
        self.__wczytaj = Button(text="Wczytaj", command=self.wczytaj)
        self.__zapisz.grid(row=22, column=22)
        self.__wczytaj.grid(row=22, column=23)
        self.__swiat = Swiat(okno = self)
        master.bind("<Left>", self.wcisnieteLewo)
        master.bind("<Right>", self.wcisnietePrawo)
        master.bind("<Up>", self.wcisnieteGora)
        master.bind("<Down>", self.wcisnieteDol)
        master.bind("<Key-u>", self.wcisnieteU)
        mainloop()
    
    def zapisz(self):
        with open('kontener.pkl', 'wb') as output:
            pickle.dump(self.__swiat.kontener, output, pickle.HIGHEST_PROTOCOL)
        with open('doDodania.pkl', 'wb') as output:
            pickle.dump(self.__swiat.doDodania, output, pickle.HIGHEST_PROTOCOL)
        with open('doUsuniecia.pkl', 'wb') as output:
            pickle.dump(self.__swiat.doUsuniecia, output, pickle.HIGHEST_PROTOCOL)
        with open('plansza.pkl', 'wb') as output:
            pickle.dump(self.__swiat.plansza, output, pickle.HIGHEST_PROTOCOL)
        with open('nrTury.pkl', 'wb') as output:
            pickle.dump(self.__swiat.numerTury, output, pickle.HIGHEST_PROTOCOL)
        with open('komunikaty.pkl', 'wb') as output:
            pickle.dump(self.__tresciKomunikatow, output, pickle.HIGHEST_PROTOCOL)
        with open('ilKomunikatow.pkl', 'wb') as output:
            pickle.dump(self.__iloscKomunikatow, output, pickle.HIGHEST_PROTOCOL)
        
    def wczytaj(self):
        for kom in self.__komunikaty:
            kom.grid_forget()
        with open('kontener.pkl', 'rb') as input:
            self.__swiat.kontener = pickle.load(input)
        with open('doDodania.pkl', 'rb') as input:
            self.__swiat.doDodania = pickle.load(input)
        with open('doUsuniecia.pkl', 'rb') as input:
            self.__swiat.doUsuniecia = pickle.load(input)
        with open('plansza.pkl', 'rb') as input:
            self.__swiat.plansza = pickle.load(input)
        with open('nrTury.pkl', 'rb') as input:
            self.__swiat.numerTury = pickle.load(input)
        with open('komunikaty.pkl', 'rb') as input:
            self.__tresciKomunikatow = pickle.load(input)
        with open('ilKomunikatow.pkl', 'rb') as input:
            self.__iloscKomunikatow = pickle.load(input)
        self.__komunikaty = []
        for kom in self.__tresciKomunikatow:
            self.__komunikaty.insert(0, Label(text=kom))
        for i in range(self.__iloscKomunikatow):
                self.__komunikaty[i].grid(row=i, column=21)
        self.__swiat.przepiszDoDodania()
        self.__swiat.aktualizujPlansze()
    
    def wcisnieteLewo(self, event):
        self.__swiat.aktualneWprowadzenie = WPROWADZENIE.STRZ_LEWO
        self.__swiat.wykonajTure()
    def wcisnietePrawo(self, event):
        self.__swiat.aktualneWprowadzenie = WPROWADZENIE.STRZ_PRAWO
        self.__swiat.wykonajTure()
    def wcisnieteGora(self, event):
        self.__swiat.aktualneWprowadzenie = WPROWADZENIE.STRZ_GORA
        self.__swiat.wykonajTure()
    def wcisnieteDol(self, event):
        self.__swiat.aktualneWprowadzenie = WPROWADZENIE.STRZ_DOL
        self.__swiat.wykonajTure()
    def wcisnieteU(self, event):
        self.__swiat.aktualneWprowadzenie = WPROWADZENIE.UMIEJETNOSC
        self.__swiat.wykonajTure()
    
    def setIkona(self, x, y, typ):
        index = 20*y + x
        if(typ == TYP_ORGANIZMU.WILK):
            self.__obrazki[index].configure(image = self.__wilk)
            self.__obrazki[index].image = self.__wilk
        elif(typ == TYP_ORGANIZMU.OWCA):
            self.__obrazki[index].configure(image = self.__owca)
            self.__obrazki[index].image = self.__owca
        elif(typ == TYP_ORGANIZMU.ZOLW):
            self.__obrazki[index].configure(image=self.__zolw)
            self.__obrazki[index].image = self.__zolw
        elif(typ == TYP_ORGANIZMU.CZLOWIEK):
            self.__obrazki[index].configure(image = self.__czlowiek)
            self.__obrazki[index].image = self.__czlowiek
        elif(typ == TYP_ORGANIZMU.ANTYLOPA):
            self.__obrazki[index].configure(image = self.__antylopa)
            self.__obrazki[index].image = self.__antylopa
        elif(typ == TYP_ORGANIZMU.LIS):
            self.__obrazki[index].configure(image = self.__lis)
            self.__obrazki[index].image = self.__lis
        elif(typ == TYP_ORGANIZMU.TRAWA):
            self.__obrazki[index].configure(image = self.__trawa)
            self.__obrazki[index].image = self.__trawa
        elif(typ == TYP_ORGANIZMU.MLECZ):
            self.__obrazki[index].configure(image = self.__mlecz)
            self.__obrazki[index].image = self.__mlecz
        elif(typ == TYP_ORGANIZMU.GUARANA):
            self.__obrazki[index].configure(image = self.__guarana)
            self.__obrazki[index].image = self.__guarana
        elif(typ == TYP_ORGANIZMU.JAGODY):
            self.__obrazki[index].configure(image = self.__jagody)
            self.__obrazki[index].image = self.__jagody
        elif(typ == TYP_ORGANIZMU.PUSTE):
            self.__obrazki[index].configure(image = self.__puste)
            self.__obrazki[index].image = self.__puste
    
    def dodajKomunikat(self, komunikat):
        if(self.__iloscKomunikatow == OknoProgramu.MAX_KOMUNIKATOW):
            self.__komunikaty.pop()
            self.__tresciKomunikatow.pop()
            self.__komunikaty.insert(0, Label(text=komunikat))
            self.__tresciKomunikatow.insert(0, komunikat)
        else:
            self.__komunikaty.insert(0, Label(text=komunikat))
            self.__tresciKomunikatow.insert(0, komunikat)
            self.__iloscKomunikatow = self.__iloscKomunikatow + 1
        
        for i in range(self.__iloscKomunikatow):
                self.__komunikaty[i].grid(row=i, column=21)
    
    def dodajRezultatWalki(self, wygrany, przegrany, numerTury):
        
        komunikat="Tura nr {nrTury} na polu: ({wygranyX},{wygranyY}) {typWygrany} zabija {typPrzegrany}.".format(
                    nrTury=numerTury, wygranyX=wygrany.aktualnePolozenie.x, wygranyY=wygrany.aktualnePolozenie.y,
                    typWygrany=wygrany.typJakoString(), typPrzegrany=przegrany.typJakoString())
        self.dodajKomunikat(komunikat=komunikat)
        
    def dodajRozmnazanie(self, wspolrzedneNowego, typ, numerTury):
        komunikat="Tura nr {nrTury} na polu ({nowyX},{nowyY}) urodzil sie nowy {typ}.".format(
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
            

root = Tk()       
app = OknoProgramu(master=root)