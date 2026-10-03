class Hayvon:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def malumot(self):
        print(f"{self.ism}, {self.yosh} yosh")

    def ovoz(self):
        print("...")


class It(Hayvon):
    def ovoz(self):
        print("Vov!")


class Mushuk(Hayvon):
    def ovoz(self):
        print("Miyov!")


class Baliq(Hayvon):
    pass


i = It("Bobik", 3)
m = Mushuk("Mosh", 2)
b = Baliq("Oltin", 1)

for x in(i, m, b):
    x.malumot()
    x.ovoz()
        