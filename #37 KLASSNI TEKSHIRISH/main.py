#37 KLASSNI TEKSHIRISH

# Klasslarni ham tekshirib turish kerak.

# KIRISH
# Avvalgi darsimizda funksiyalarni tekshiruvchi testlar yozishni o'rgandik. Ushbu mavzuda esa klasslarni test qilishni o'rganamiz. Klass to'g'ri bo'lsa, undan yaratilgan obyektlar ham to'g'ri ishlaydi.
# Keling boshlanishiga biror klass yaratamiz:

class Car:
    """(self, make, model, year, km=0, price=None)"""
    def __init__(self, make, model, year, km=0, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km

    def set_price(self, price):
        self.price = price

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")

    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year} - yil, {self.__km}km yurgan."
        if self.price:
            info += f" Narhi: {self.price}"
        return info

    def get_km(self):
        return self.__km

# Yuqoridagi klassimiz avtomobil haqida ma'lumotlarni saqlaydi. Klassimizning e'tibor qaratishimiz kerak bo'lgan jihatlari:
# km va price (narh) argumentlariga standart qiymat berilgan
# km parametri inkapsulasiyalangan (self.__km)
# Avtomobil narhini set_price() metodi yordamida yangilash mumkin
# add_km() metodi faqat musbat qiymat qabul qiladi. Agar manfiy qiymat uzatilsa raise operatori yordamida ValueError xatosini qaytaradi
# get_info() metodidan qaytadigan qiymat avtomobil narhi bor yoki yo'qligiga qarab turli ko'rinishda bo'lishi mumkin
# Avtomobil kilometrajini ko'rish uchun get_km() metodiga murojat qilamiz.

# XUSUSIYATLARNI TEKSHIRISH
# Klassdan obyekt yaratish jarayonida biz obyektning xususiyatlarini parametr ko'rinishida beramiz. Quyidagi testda aynan shu jarayon to'g'ri kechganini tekshiramiz:

