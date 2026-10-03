class Karta:
    def __init__(self, egasi, pin):
        self.egasi = egasi
        self.__pin = pin          # yopiq xususiyat
        self.__balans = 0          # yopiq xususiyat
        self.__urinishlar = 0        # yopiq xususiyat
        self.__bloklangan = False     # yopiq xususiyat

     # Yopiq (private) metod
    def __pin_togrimi(self, pin):
        if pin == self.__pin:
            self.__urinishlar = 0
            return True
        
        else:
            self.__urinishlar += 1

        if self.__urinishlar >= 3:
            self.__bloklangan = True
            print("Karta bloklandi")
            return False
    
    # To'ldirish metodi
    def toldirish(self, summa):
        self.__balans += summa
        print(f"Balans: {self.__balans}")

     # Yechish metodi
    def yechish(self, pin, summa):
        if self.__pin_togrimi:
            print("Karta bloklangan")
        elif not self.__pin_togrimi (pin):
            print("PIN noto'g'ri")
        elif summa > self.__balans:
            print("Mablag' yetarli emas")
        else:
            print(f"{summa} so'm yechildi. Balans: {self.__balans}")

     # Balansni korish metodi
    def balansni_korish(self, pin):
        if self.__bloklangan:
            print("Karta bloklandi")
        elif not self.__pin_togrimi((pin)):
            print("Pin noto'g'ri")
        else:
            print(f"Balans: {self.__balans}")

        
k = Karta("Ali", "1234")
k.toldirish(500000)
k.yechish("1234", 200000)
k.yechish("0000", 1000)
k.yechish("1111", 1000)
k.balansni_korish("9999")
k.yechish("1234", 1000)

