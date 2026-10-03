class Xodim:
    def __init__(self, ism, oylik):
        self.ism = ism
        self.oylik = oylik

    def yillik(self):
        return (self.oylik * 12)

    def malumot(self):
        print(f"{self.ism}: oylik {self.oylik}, yillik {self.yillik()}")


class Menejer(Xodim):
    def __init__(self, ism, oylik, bonus):
        super().__init__(ism, oylik)
        self.bonus = bonus
    
    def yillik(self):
       oddiy_yillik = super().yillik()
       bonus_summasi = oddiy_yillik * (self.bonus / 100)
       return oddiy_yillik + bonus_summasi
    

class Dasturchi(Xodim):
    def __init__(self, ism, oylik):
        super().__init__(ism, oylik)
        self.tillar = []

    def til_qosh(self, til):
        self.til = til
        self.tillar.append(til)

    def malumot(self):
        super().malumot()
        tillar_str = ", ".join(self.tillar)
        print(f"Tillar: {self.tillar, }")

       

x1 = Xodim("Ali", 5000000)
m1 = Menejer("Malika", 9000000, 20)
d1 = Dasturchi("Sardor", 12000000)

d1.til_qosh("Python")
d1.til_qosh("SQL")

xodimlar = (x1, m1, d1)

for i in xodimlar:
    i.malumot()
    

# Barcha xodimlarning yillik maoshlari yig'indisi
jami_yillik = sum(i.yillik() for i in xodimlar)
print(f"Jami yillik maosh: {int(jami_yillik)} so'm")