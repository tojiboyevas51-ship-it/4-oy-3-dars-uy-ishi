from abc import ABC, abstractmethod

class Shakl(ABC):

    
    @abstractmethod
    def yuza(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def malumot(self):
        print(f"{self.nomi}: yuza  = {self.yuza()}, perimetr = {self.perimetr()}")

class Tortburchak(Shakl):
    def __init__(self, eni, boyi):
        self.nomi = "To'rtburchak"
        self.eni = eni
        self.boyi = boyi
    
    def yuza(self):
        return self.eni * self.boyi
    

    def perimetr(self):
        return 2 * (self.eni + self.boyi)
    

class Doira(Shakl):
    nomi = "Doira"
    def __init__(self, radius):
        self.radius = radius

    
    def yuza(self):
        return (3.14 * self.radius ** 2)
    

    def perimetr(self):
        return (2 * 3.14 * self.radius)
    
t1 = Tortburchak(4, 3)
d1 = Doira(2)

shakllar = [t1, d1]

for x in(t1, d1):
    x.malumot()
