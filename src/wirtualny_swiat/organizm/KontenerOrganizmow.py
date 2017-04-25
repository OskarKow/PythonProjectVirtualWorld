


class KontenerOrganizmow:
    def __init__(self):
        self.__iloscOrganizmow = 0
        self.__organizmy = []
    
    @property
    def iloscOrganizmow(self):
        return self.__iloscOrganizmow
    
    def getOrganizm(self, index):
        return self.__organizmy[index]
    
    def dodajOrganizm(self, organizm):
        self.__iloscOrganizmow = self.__iloscOrganizmow + 1
        self.__organizmy.append(organizm)
        self.__posortujOrganizmy()
        
    def usunOrganizm(self, organizm):
        if(self.__iloscOrganizmow > 0):
            self.__iloscOrganizmow = self.__iloscOrganizmow - 1
            self.__organizmy.remove(organizm)
    
    def __porownajOrganizmy(self, organizmA, organizmB):
        if(organizmA.inicjatywa > organizmB.inicjatywa):
            return True
        if(organizmA.inicjatywa < organizmB.inicjatywa):
            return False
        if(organizmA.wiek >= organizmB.wiek):
            return True
        else:
            return False
    
    def __posortujOrganizmy(self):
        for i in range(self.__iloscOrganizmow - 1):
            for j in range(self.__iloscOrganizmow - 1):
                if(self.__porownajOrganizmy(organizmA=self.__organizmy[j], organizmB=self.__organizmy[j + 1]) == False):
                    tmp = self.__organizmy[j + 1]
                    self.__organizmy[j+1] = self.__organizmy[j]
                    self.__organizmy[j] = tmp
    
    def wyczysc(self):
        self.__iloscOrganizmow = 0
        self.__organizmy = []
    
    def czyZawiera(self, organizm):
        for org in self.__organizmy:
            if(org is organizm):
                return True
        return False
    
    @property
    def organizmy(self):
        return self.__organizmy
    