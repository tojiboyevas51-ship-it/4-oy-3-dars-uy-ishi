class Foydalanuvchi:
  def __init__(self, login, parol):
    self.login = login       # ochiq xususiyat
    self.__parol = parol     # yopiq xususiyat(inkapsulyatsiya qilingan)


  def parolni_tekshir(self, parol):
    if parol == self.__parol:
      return True
    else:
      return False


  def parolni_ozgartir(self, eski, yangi):
    self.eski = eski
    if not self.parolni_tekshir(eski):
      print("Eski parol noto'g'ri")

    elif len(yangi) < 6:
      print("Parol kamida 6 ta belgidan iborat bo'lishi kerak")

    else:
      self.__parol = yangi
      print("Parol o'zgartirilidi")


u = Foydalanuvchi("ali_01", "qwerty")
print(u.parolni_tekshir("12345"))
u.parolni_ozgartir("111111", "abcdef")
u.parolni_ozgartir("qwerty", "abc")
u.parolni_ozgartir("qwerty", "yangi123")
print(u.parolni_tekshir("yangi123"))
