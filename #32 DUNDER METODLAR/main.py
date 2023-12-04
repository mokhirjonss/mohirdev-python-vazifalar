#32 DUNDER METODLAR
from os import name


# Pythondagi maxsus metodlar bilan tanishamiz.

# MAXSUS METODLAR

# Pythonda obyektlar bilan ishlashni yanada qulay qilish uchun bir nechta maxsus metodlar bor. Bu metodlarning nomi ikki pastki chiziq bilan yozilgani uchun, double underscore yoki qisqa qilib dunder metodlar deb ataladi. Dunder metolar yordamida obyektlarga qo'shimcha qulayliklar va vazifalar qo'shishimiz mumkin. Klass yoki obyektga oid dunder metodlar ro'yxatini ko'rish uchun dir() funksiyasidan foydalanamiz:

# >>> dir(Avto)
# ['_Avto__num_avto',
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'make',
#  'model',
#  'narh',
#  'rang',
#  'yil']

# Dunder metodlardan biz __init__ metodi bilan tanishdik. Bu metod klassdan obyekt yaratishda chaqiriladi va obyektning xususiyatlarini belgilaydi. Ushbu darsimizda esa maxsus metodlarning ba'zilari bilan tanishamiz.

# OBYEKT HAQIDA MA'LUMOT

# Obyektga print() yoki str() orqali murojat qilinganda obyekt haqida tushunarli ma'lumot qaytarish uchun __repr__va __str__ metodlaridan foydalanamiz. Tushunarli bo'lishi uchun avvalgi darsimizdagi Avto klassiga qaytamiz:

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""

    def __init__(self, make, model, rang, yil, narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def __str__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"

    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"

    def __eq__(self, boshqa_avto):
        return self.narh == boshqa_avto.narh

    def __lt__(self, boshqa_avto):
        return self.narh < boshqa_avto.narh

    def __le__(self, boshqa_avto):
        return self.narh <= boshqa_avto.narh

    def get_info(self):
        return (
            f"{self.rang} {self.make} {self.model}.{self.yil}-yil. Narhi:{self.narh}$"
        )


# Yuqoridagi klassdan yangi obyekt yaratamiz va obyekt haqida ma'lumot olish uchun print() funksiyasini chaqiramiz:

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
print(avto1) # obyekt haqida ma'lumot
# <__main__.Avto object at 0x1030b8f50>

# Qandaydur tushunarsiz ma'lumot. Ekrandagi natijadan biz faqat avto1 obyektimiz Avto klassiga tegishli ekanini ko'ramiz. Qanday qilib shuning o'rniga obyekt haqida tushunarliroq ma'lumot olishimiz mumkin?

# Gap shundaki biz har gal obyketga print() (yoki str() yoki repr()) orqali murojat qilganimizda, Python obyket ichida __str__ yoki __repr__ metodlariga murojat qiladi. Agar biz bu metodlarni yozmagan bo'lsak, yuqoridagi kabi umumiy ma'lumot qayataradi.

# Biz ushbu metodlarni yangidan yozib, biz istagan ma'lumotni qayataradian qilishimiz mumkin. Odatda, yuqoridagi ikki metoddan birini yozish kifoya. Odatda, __repr__ umumiyorq, __str__ esa batafsilroq ma'lumot olish uchun ishlatiladi.

# Ikkalasidan birini tanlaganda, __repr__metodiga yon bosiladi, sababi bu metod print(), str() va repr() funksiyalarining hammasi bilan ishlaydi. Keling biz ham yuoqirdagi klassimizga__repr__metodini qo'shamiz:

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self, make, model, rang, yil, narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
#
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto: {self.rang} {self.make} {self.model}"


    # Qaytadan print() funksiyasini chaqiramiz
#     avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
#     print(avto1)
    # Avto: Qora GM Malibu

    # Mana endi natijamiz ancha tushunarli ko'rinishda chiqdi.

    # OBYEKTLARNI TAQQOSLASH

    # Taqqoslash operatorlari yordamida biz turli obyektlarni solishtirishimiz mumkin. Taqqoslash natijasi mantiqiy qiymat (True yoki False) ko'rinishida bo'ladi.

#     x, y = 5, 10
#     print(x > y)
    # False

    # Keling endi Avto klassidan 2 ta obyekt yaratamiz, va ularni taqqoslab ko'ramiz:

#     avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
#     avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)

    # avto1>avto2
    # Natija: TypeError: '>' not supported between instances of 'Avto' and 'Avto'
    # Xatolik. Demak bu ikki obyektni solshtirib bo'lmas ekan.

    # Biz taqqolash operatorlariga murojat qilganimizda, Python obyektlar ichida taqqoslash uchun maxsus metodlarni qidiradi, agar metodlar topilmasa yuqoridagi kabi TypeError qaytaradi.

    # Taqqoslash metodlari quyidagilardan iborat:

    # x.__lt__(self,y)   x < y
    # x.__le__(self,y)   x <= y
    # x.__gt__(self,y)   x > y
    # x.__ge__(self,y)   x >= y
    # x.__eq__(self,y)   x == y
    # x.__ne__(self,y)   x ! = y

    # Yuqoridagi obyektlardan yarmi uchun metodlar yozishimiz kifoya, misol uchun __lt__ (x<y) metodini yozsak, __gt__ (x>y) metodini yozishimiz shart emas, yoki __le__ metodi, __ge__metodini ham o'z ichiga oladi, va hokazo.

    # Keling tushunarli bo'lishi uchun Avto klassiga obyektlarni solishtirish uchun metod yozamiz. Deylik, biz obyektlarni narhi bo'yicha solishtirmoqchimiz, unda klassimizga quyidagi metodlarni qo'shamiz (klassni to'liq yozmadik, faqat qo'shilgan metodlarni keltiramiz):

#     def __eq__(self, boshqa_avto):
#         """Tenglik"""
#         return self.narh == boshqa_avto.narh
#
#     def __lt__(self, boshqa_avto):
#         """Kichik"""
#         return self.narh < boshqa_avto.narh
#
#     def __le__(self, boshqa_avto):
#         """Kichik yoki teng"""
#         return self.narh <= boshqa_avto.narh

# Kodimizga e'tibor qilsangiz biz tenglik (__eq__) yoki kichiklikni (__lt__) tekshirmoqchi bo'lganimizda ikki avtoning aynan narhi bo'yicha solishtiramiz (self.narh == boshqa_avto.narh).

# Mana endi avtolarni solishtirsak bo'ladi:

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
print(avto1 > avto2)
# True

avto3 = Avto("Honda", "Accord", "Oq", 2017, 40000)
print(avto1 == avto3)
# True

# OBYEKT UZUNLIGI

# Pythonda len() funksiyasi yordamida turli obyektlarning uzunligini bilishimiz mumkin, misol uchun matn, ro'yxat, lug'at, set va hokazo.
matn = 'hello world'
print(len(matn))
# 11

sonlar = [12, 34, 56, 66]
print(len(sonlar))
# 4

# Biz len() funksiyasiga murojat qilganimizda, Python funksiyaga uzatilgan obyektning ichidagi maxsus __len__ metodiga murojat qiladi. Agar bu metod mavjud bo'lmasa dasturimiz xato qaytaradi.

# len(avto1)
# Natija: TypeError: object of type 'Avto' has no len()
# Misol uchun, bizning Avto klassimizda bu metod yozilmagan, shuning uchun Python TypeError xatosini qaytardi.
# Kelin endi __len__metodini qanday ishlatishga ham misol ko'raylik.
# Boshlanishiga, yangi, AvtoSalon degan klass yaratamiz. Bu klassimiz 2 ta xususiyatga ega: salon nomi (name) va salondagi mashinalar (avtolar).

class AvtoSalon:
    """Avtosalon klassi"""

    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index] = value

    def __add__(self, qiymat):
        if isinstance(qiymat, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat, Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

    def __call__(self, *param):
        if param:
            for avto in param:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def get_list(self):
        return [avto for avto in self.avtolar]


# Yuqoridagi klassdan yangi obyekt yaratamiz:

salon1 = AvtoSalon("MaxAvto")
print(salon1)
# MaxAvto avtosaloni

# AvtoSalon klassimizga __repr__metodini qo'shganimiz uchun natijamiz chiroyli ko'rinishda chiqdi.
# Keling endi salonga avtomobil qo'shish uchun yangi add_avto() metodini yozamiz. Bu metodimiz Avto klassiga oid obyektlarni qabul qilishi kerak. add_avto() ga uaztilgan parametr Avto klassiga tegishli yoki yo'qligini tekshirish uchun maxsus isinstance() funksiyasidan foydalanamiz.

# Bu funksiya biror obyekt ma'lum klassga tegishli ekanligini tekshirish uchun ishlatiladi:

print(isinstance("salom", str))
# True # "salom" bu str
print(isinstance(9.5, int))
# False # 9.5 int (butun son) emas
print(isinstance(avto1, Avto))
# True # avto1 Avto klassiga tegishli

# add_avto() metodiga qaytamiz:


# Metodimizni tekshirib ko'ramiz

# Avto obyektlarini yaratamiz
# avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
# avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
# avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)

# Yuqoridagi obyektlarni salon1 ga qo'shamiz
# for avto in [avto1, avto2, avto3]:
#     salon1.add_avto(avto)

# Mana navbat __len__ metodiga. Biz bu metod yordamida len() funksiyasi salonimizdagi avtomobillar sonini qaytaradigan qilamiz. Buning uchun yuqoridagi AvtoSalon klassiga __len__ funksiyani ham qo'shamiz va uni obyekt ichidagi avtolar ro'yxatyining uzunligini qaytaradigan qilamiz:


# Mana endi bizning AvtoSalon klassimizga oid obyektlar uchun ham len() funksiyasini qo'llasak bo'ladi:

# OBYEKT ELEMENTLARIGA MUROJAT QILISH

# Ba'zi obyektlarning (matn, ro'yxat, lug'at va hokazo) elementlariga alohida murojat qilish mumkin.
mevalar = ['olma', 'anor', 'uzum']
print(mevalar[0])
# olma

# Bizning salonimizda ham 3 ta avto bor, ularni ko'rish uchun yuqoridagi kabi element raqami orqali murojat qila olamizmi?

# salon1[0]
# Natija: TypeError: 'AvtoSalon' object is not subscriptable

# Afsuski yo'q. Ko'rib turganingizdek bizning obyektimizga bunday murojat qilib bo'lmas ekan. Obyektimizga bu xususiyatni qo'shish uchun __getitem__metodini yozishimiz kerak.



# Endi salon1 obyektimizning elementlariga murojat qilinganda __getitem__metodi obyekt ichidagi avtolar ro'yxatidan ko'rsatilgan element (avtomobilni) qaytaradi.

# print(salon1[0])
# # Avto: Qora GM Malibu
# print(salon1[1])
# Avto: Oq GM Lacetti

# Keling obyekt elementlaridan birini o'zgartirib ko'ramiz:
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# salon1[0]=avto4
# Natija: TypeError: 'AvtoSalon' object does not support item assignment

# Yana xatolik. Gap shundaki __getitem__ metodi o'z nomi bilan (get) element qaytaruvchi metod. Biror elementni o'zgartirish uchun esa __setitem__metodini ham qo'shishimiz kerak. Bu metodimizga murojat qilinganda ham, yangi qiymat Avto klassiga oid ekanligini tekshirib olish maqsadga muvofiq bo'ladi:

#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value

# Qaytadan elementni o'zgartirishga harakat qilib ko'ramiz:

# avto4 = Avto("Mazda", "6", "Qizil", 2015, 35000)
# salon1[0] = avto4
# print(salon1[0])

# Avto: Qizil Mazda 6

# Kutilgan natija chiqdi

# OPERATORLARNI QAYTA TALQIN QILISH (OVERLOADING)

# Pythonda obyektlar o'rtasida turli arifmetik amallarni bajarish mumkin va bu amallar obyektning turiga qarab, Pytnon tomonidan turlicha talqin qilinadi. Masalan:

# sonlar:

x, y = 10, 20
print(x + y)
# 30

# Matnlar:
t1 = "hello"
t2 = "world"
print(t1 + t2)
# helloworld

# Keling, bu amallarni bizning obyektimizga ham qo'llab ko'ramiz. Boshlanishiga 2 ta avtosalon yarataylik, va har biriga alohida avtolar qo'shaylik. Ishimizni osonlashtirish uchun add_avto() metodimizni ham istalgancha parametr qabul qilishga moslab o'zgartiramiz:

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []
#
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#
#     def __len__(self):
#         return len(self.avtolar)
#
#     def __getitem__(self,index):
#         return self.avtolar[index]
#
#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value
#
#     def add_avto(self,*qiymat):
#         for avto in qiymat:
#             if isinstance(avto,Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyketini kiriting")

# Obyektlarni yaratamiz:
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)

# Mavzuga qaytamiz. Operatorlarni qayta talqin qilish. Keling boshlanishiga ikki obyektni qo'shib ko'ramiz:

# salon1+salon2
# Natija: TypeError: unsupported operand type(s) for +: 'AvtoSalon' and 'AvtoSalon'

# Demak, bu ikki obyektni qo'shib bo'lmas ekan. Biz obyekt egasi sifatida qo'shish operatorini o'zimiz istagancha talqin qilishimiz mumkin. Misol uchun AvtoSalon obyektiga boshqa AvtoSalon obyektini qo'shganda, yangi AvtoSalon obyektini qaytaraylik va bu yangi obyekt avvalgi ikki obyektning avtolariga ega bo'lsin.
# Qo'shish operatorini qayta talqin qilish uchun AvtoSalon klassimizga __add__ metodini qo'shamiz.
#     def __add__(self,qiymat):
#         if isinstance(qiymat,AvtoSalon):
#             yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
# Qo'shish operatorini tekshirib ko'ramiz:

salon3 = salon1 + salon2
print(salon3)
# MaxAvto Avto Lider avtosaloni

# Istasak, qo'shish operatori yordamida salonga yangi Avto qo'shish imkoniyatini ham yaratishimiz mumkin:

#     def __add__(self,qiymat):
#         if isinstance(qiymat,AvtoSalon):
#             yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
#         elif isinstance(qiymat,Avto):
#             self.add_avto(qiymat)
#         else:
#             print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

# Tekshirib ko'ramiz:
avto7 = Avto("BMW", 'X7','Qora',2015,75000)
salon1 + avto7
print(salon1[:])
# [Avto: GM Malibu. 40000$, Avto: GM Lacetti. 20000$, Avto: Toyota Carolla. 45000$, Avto: BMW X7. 75000$]

