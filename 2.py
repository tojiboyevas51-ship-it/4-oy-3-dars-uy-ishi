class Mahsulot:
  def __init__(self, nomi, narx, soni):
    self.nomi = nomi         # ochiq xususiyat
    self.__narx = narx       # yopiq xususiyat
    self.__soni = soni       # yopiq xususiyat

  def narxni_ol(self):
    return self.__narx

  def sonini_ol(self):
    return self.__soni

  def narxni_ber(self, narx):
    if narx > 0:
      self.__narx == narx
      print("O'rnatildi")
    else:
      print("Narx musbat bolishi kerak")

  def sotish(self, miqdor):
    if miqdor > self.__soni:
      print(f"Omborda faqat {self.__soni} ta bor")
    else:
      self.__soni -= miqdor
      jami = miqdor * self.__narx
      print(f"{miqdor} ta sotildi. Jami: {jami} so'm")


m = Mahsulot("Daftar", 5000, 20)
m.sotish(3)
m.narxni_ber(-100)
m.narxni_ber(6000)
m.sotish(30)
m.sotish(17)
print(m.sonini_ol)
