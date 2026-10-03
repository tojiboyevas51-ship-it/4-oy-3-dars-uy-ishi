class Chiroq:

    def __init__(self, xona):
        self.xona = xona

    def yoqish(self):
        print(f"{self.xona}: chiroq yondi")

    def ochirish(self):
        print(f"{self.xona}: chiroq o'chdi")


class Konditsioner:

    def __init__(self, harorat):
        self.harorat = harorat

    def yoqish(self):
        print(f"Konditsioner yoqildi: {self.harorat}°C")

    def ochirish(self):
        print("Konditsioner o'chirildi")


class Televizor:

    def __init__(self, kanal):
        self.kanal = kanal

    def yoqish(self):
        print(f"Televizor yoqildi, kanal: {self.kanal}")

    def ochirish(self):
        print("Televizor o'chirildi")


# Funksiya klassdan tashqarida bo'lishi kerak
def hammasini_yoq(qurilmalar):
    for qurilma in qurilmalar:
        qurilma.yoqish()


def hammasini_ochir(qurilmalar):
    for qurilma in reversed(qurilmalar):
        qurilma.ochirish()


class Choynak:

    def yoqish(self):
        print("Choynak qaynayapti")

    def ochirish(self):
        print("Choynak o'chdi")


uy = [Chiroq("Mehmonxona"), Konditsioner(22), Televizor("Sport"), Choynak()]

hammasini_yoq(uy)
print("--- uxlash vaqti ---")
hammasini_ochir(uy)