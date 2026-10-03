class Transport:
    def __init__(self, brend, tezlik):
        self.brend = brend
        self.tezlik = tezlik

    def malumot(self):
        print(f"{self.brend}: {self.tezlik} km/soat")


class Mashina(Transport):
    def __init__(self,brend, tezlik, orindiqlar):
        super().__init__(brend, tezlik)
        self.orindiqlar = orindiqlar

    def malumot(self):
        super().malumot()
        print(f"O'rindiqlar: {self.orindiqlar}")

    
class YukMashinasi(Mashina):
    def __init__(self, brend, tezlik, orindiqlar, yuk_hajmi):
        super().__init__(brend, tezlik, orindiqlar)
        self.yuk_hajmi = yuk_hajmi

    def malumot(self):
        super().malumot()     # Ota metodni chaqiramiz
        print(f"Yuk: {self.yuk_hajmi} tonna")

    def yuklash(self, tonna):
        if tonna > self.yuk_hajmi:
            print("Juda og'ir!")
        else:
            print(f"{tonna} tonna yuklandi")


m = Mashina("Malibu", 220, 5)
y = YukMashinasi("Isuzu", 120, 3, 8)

m.malumot()
y.malumot()
y.yuklash(10)
y.yuklash(6)
print(isinstance(y, Transport))

