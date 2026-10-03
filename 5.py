from abc import ABC, abstractmethod

class Hisob(ABC):

    def __init__(self, egasi):
        self.egasi = egasi   # ochiq xususiyat
        self.__balans = 0    # yopiq xususiyat

    def balansni_ol(self):
        return self.__balans 

    def kiritish(self, summa):
        self._ozgartir(summa)

    def _ozgartir(self, summa):
         self.__balans += summa

    @abstractmethod
    def yechish(self,summa):
        pass


class JamgarmaHisobi(Hisob):
    def __init__(self, egasi, foiz):
        super().__init__(egasi)
        self.foiz = foiz

    
    def yechish(self, summa):
        if summa > self.balansni_ol():
            print("Mablag' yetarli emas")
        else:
            self._ozgartir(-summa) 

    def foiz_qosh(self):
        foiz_summasi = self.balansni_ol() * (self.foiz / 100)
        self._ozgartir(foiz_summasi) 
        print(f"Foiz qo'shildi: {foiz_summasi}")


class KreditHisobi(Hisob):
    def __init__(self, egasi, limit):
        super().__init__(egasi)
        self.limit = limit

    
    def yechish(self,summa):
        if self.balansni_ol() - summa < -self.limit:
            print("Kredit limiti oshdi")
        else:
            self._ozgartir(-summa)


j = JamgarmaHisobi("Ali", 10)
k = KreditHisobi("Vali", 1000000)

j.kiritish(500000)
j.yechish(700000)
j.foiz_qosh()

k.kiritish(200000)
k.yechish(1000000)
k.yechish(500000)

print(f"{j.egasi}: {j.balansni_ol()}")
print(f"{k.egasi}: {k.balansni_ol()}")

