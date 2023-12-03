#30 VORISLIK VA POLIMORFIZM

# Klasslardan klass yaratishni o'rganamiz.

# SUPER KLASS VA VORIS KLASS

# Obyektga yo'naltirilgan dasturlashning qulayliklaridan biri bu klasslardan boshqa klass yaratish imkoniyati. Bizga kerak bo'lgan yangi klass, avval yaratilgan boshqa klass bilan o'xshashlik joylari bo'lsa, biz bu klassdan voris klass yaratishimiz mumkin. Bunda asl klass - ota, yoki super klass deb ataladi.

# Super klassdan yaratilgan voris klass otaning barcha yoki tanlangan xususiyatlari va metodlarini meros olish bilan birga, o'ziga xos xususiyat va metodlariga ega bo'ladi.

# Keling boshlanishiga Shaxs klassini yaratamiz, bu klassimiz keyinchalik boshqa klasslar uchun super klass vazifasini bajaradi:

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ulgan."
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

# Klassimizni tekshirib ko'ramiz:

inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
# Hasan Alimov. Passport: FB001122, 1995-yilda tug'ulgan.. 26 yoshda.

# VORIS KLASS YARATISH

# Endi avvalgi darsimizda yaratgan Talaba klassimizni qaytadan yaratamiz. Bu safar, avvalgidan farqli ravishda, Talaba ni yaratishda, Shaxs dan super klass sifatida foydalanamiz:

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)

# Kodimizni tahlil qilaylik:

# 1-qatorda klass nomidan so'ng, qavs ichida super klass nomini berdik
# 5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik

# Yangi yaratgan Talaba klassimiz Shaxsning barcha xususiyatlari va metodlariga ega bo'ladi.

talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000)
print(talaba.get_info())
# Valijon Aliyev. Passport: FA112299, 2000-yilda tug'ulgan.

# Valijon Aliyev. Passport: FA112299, 2000-yilda tug'ulgan.

# Huddi shu kabi get_age() metodiga ham murojat qilishimiz mumkin:

print(talaba.get_age(2021))
# 21

# Dastur davomida super klass voris klasslardan avval yozilgan (chaqirilgan) bo'lishi kerak.

# VORIS KLASSGA XOS XUSUSIYATLAR VA METODLAR

# Hozirgi ko'rinishda Talaba va Shaxs klasslari o'rtasida hech qanday farq yo'q. Keling Talaba klassimizga o'ziga xos xususiyatlar va metodlar yarataylik. Avvalosiga, talabaning bosqichi va ID raqamini xususiyat sifatida qo'shamiz. Bunda ID raqami obyekt yaratilishida parameter sifatida uzatiladi, bosqich esa standart qiymatga ega.

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1

    def get_id(self):
        pass

    def get_bosqich(self):
        pass


# Endi yangi, Talaba obyektini yaratishda qo'shimcha idraqam parametrini ham kiritish talab qilinadi:

talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012")

# So'ngra, bu qiymatlarni qaytaruvchi alohida metodlar yozamiz:

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

# Metodlarni tekshirib ko'ramiz:

print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
print(f"{talaba.get_bosqich()}-bosqich talabasi")

# Shu zayilda yangi klassimizga istalgancha yangi xususiyatlar va metodlar qo'shishimiz mumkin. Bunda, agar yangi xususiyat yoki metod super klassga ham aloqador bo'lsa uni birdan super klassga qo'shish tavsiya qilinadi.

# Voris klass boshqa klass uchun super klass bo'lishi mumkin.

# POLIMORFIZM — SUPER KLASS METODLARINI QAYTA YOZISH

# Voris klassga super klassdan meros qolgan istalgan metodni qayta talqin qilish mumkin. Avvalgi misolimizdagi get_info() super metodini ko'raylik, bu metod talabaning ismi, familiyasi, passport raqami va tug'ilgan yilini qaytaradi:

print(talaba.get_info())
# Valijon Aliyev. Passport: FA112299, 2000-yilda tug'ulgan.

# Endiget_info() metodi talabaga mos ma'lumotlar qaytarishi uchun, Talaba klassi ichida huddi shu nomli metodni qayta yozamiz:

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}"
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

# Metodni tekshirib ko'ramiz:
print(talaba.get_info())

# OBYEKT ICHIDA OBYEKT

# Ba'zida klassimiz xususiyatlar va ular bilan ishlaydigan metodlarga to'lib ketishi, bu esa o'z navbatida obyektga murojat qilishni qiyinlashitirishi mumkin. Shunday holatlarda ba'zi xususiyatlarni alohida klass ko'rinishida yozish va keyinchalik bu klassdan yaratilgan obyektni boshqa obyektning xususiyati sifatida foydalanish mumkin.

# Misol uchun, yuqoridagi Shaxs klassimizga yana bir manzil degan xususiyat qo'shaylik. Odatda manzil bir nechta qismlardan iborat bo'ladi (xonadon, ko'cha, mahalla, tuman/shahar, viloyat, indeks va hokazo) va ularning har biri uchun Shaxs ichida alohida xususiyat yaratmasdan, alohida manzil degan klassga yuklash maqsadga muvofiq bo'ladi.

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman}"
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

# Talaba klassimizga ham qo'shimcha manzil xususiyatini qo'shamiz:

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

# Keling endi talaba obyektini qayta yaratamiz. Bu safar talabaning manzili ham alohida obyekt sifatida talaba ga uzatiladi:

talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)

# Obyekt ichidagi obyektning xususiyatlari va metodlariga ham avvalgidek nuqta orqali murojat qilishimiz mumkin:

print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)


