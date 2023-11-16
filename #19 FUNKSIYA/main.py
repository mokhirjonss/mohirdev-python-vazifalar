# #19 FUNKSIYA
# Pythonda funksiyalar bilan tanishamiz

# FUNKSIYA NIMA?
# Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi. Biz shu paytgacha bir nechta tayyor funksiyalardan foydalanib keldik. Misol uchun print() funksiyasi konsolga matn chiqarish uchun, range() funksiyasi esa ma'lum oraliqdagi sonlarni yaratish uchun ishlatiladi.
# Aslida har qanday funksiyaning ortida ham bir necha qatordan iborat kod bo'ladi, lekin biz funksiyaga murojat qilganda uning nomini yozamiz xolos. Funksiya ortidagi kod esa biz uchun yashirin bo'lib qolaveradi. Funksiyalarning qulayligi ham shunda. Dastur davomida ma'lum bir kodlarni qayta-qayta yozmaslik uchun biz ularni jamlab, bitta funksiya ichiga joylashimiz va dastur davomida bu kodlarga funksiya nomi orqali murojat qilishimiz mumkin.
# Funksiyalar turlicha bo'ladi, ba'zi funksiyalar sizdan qiymat qabul qilib, konsolga biror ma'umot chiqaradi, ba'zilari esa sizdan qabul qilgan qiymat ustida turli amallar bajarib yangi qiymat qaytaradi. Foydalanuvchidan mutlaqo qiymat qabul qilmaydigan funksiyalar ham mavjud.
# Ushbu mavzuda siz qanday qilib Pythonda yangi funksiya yaratish, unga murojat qilish, tekshirish va to'g'rilashni o'rganasiz. Shuningdek darsimiz yakunida dasturimizni bir nechta faullarga ajratishni va funksiylarani alohida, module deb ataluvchi fayllarga joylashni ham o'rganamiz.

# FUNKSIYA YARATAMIZ
# Keling oddiy, salom_ber deb nomlangan funksiya yaratamiz. Bu funksiya murojat qilganimizda konsolga "Assalom alaykum!" degan xabarni chiqarsin.

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber()
# Assalomu alaykum!

# Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.

# FUNKSIYAGA QIYMAT UZATISH
# Avvalgi sodda funksiyamiz foydalanivchidan hech qanday qiymat olmaydi va barchaga birday "Assalomu alaykum!" deb javob qiladi. Keling funksiyaga o'zgartirish kiritamiz, funksiya foydalanuvchi ismini qabul qilib, unga ismi bilan murojat qilsin. Buning uchun funksiya nomidan keyin, qavs ichida foydalanuvchi berishi kerak bo'lgan qiymatni ko'rsatamiz.

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomi alaykum, hurmatli {ism.title()}!")

salom_ber('mokhirjon')
# Assalomi alaykum, hurmatli Mokhirjon!
salom_ber('dilshod')
# Assalomi alaykum, hurmatli Dilshod!

# Agar funksiyaga murojat qilishda, unga qiymat bermasak xatolik vujudga keladi:
# salom_ber()
# Natija: TypeError: salom_ber() missing 1 required positional argument: 'ism'


# DOCSTRING
# Avval aytganimizdek, funksiya yaratganda, funksiya qanday ishlashi haqida qisqacha ma'lumot berib ketish o'zimiz uchun ham, kelajakda bizni funksiyamizni ishlatadigan boshqa dasturchilar uchun ham juda foydali bo'ladi. Quyidagi funksiyaning 2-qatorda biz funksiya haqida ma'lumot berdik. Bu qator docstring deyiladi. Murakkab funksiyalar uchun docstringni bir necha qatorga bo'lib yozishingiz mumkin

# Xo'sh, bu ma'lumot qachon va qayerda ko'rsatiladi? Dastur yozish jarayonida funksiya nomini yozishingiz bilan, docstring ko'rsatiladi:

# Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin:

print(salom_ber.__doc__)

#  FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH
# Funksiya yaratishning asl maqsadlaridan biri, biz unga qayta-qayta, yangi qiymatlar bilan murojat qilishimiz mumkin.

salom_ber('hasan')
salom_ber('olim')
# Assalomi alaykum, hurmatli Hasan!
# Assalomi alaykum, hurmatli Olim!

# ARGUMENT VA PARAMETER
# Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat parameter deb ataladi. Yuqoridagi misolda ism bu salom_ber funksiyasining parametri.
# Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument deb ataladi. salom_ber('hasan') kodida 'hasan' bu argument.

# Ba'zi manbalarda yoki darslarda argument va parametr so'zlari almashtirib ishlatilishi ham kuzatiladi.

# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
# Shunday funksiyalar bor, bir emas bir nechta parameter talab qilishi mumkin, foydalanuvchi esa o'z navbatida bir nechta argumentlar taqdim qilishi kerak. Funksiyaga argument uzatishning bir necha usuli bor, keling ular bilan birma bir tanishamiz.

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchini ismi: {ism.title()}\n"
          f"Foydalanuvchini familiyasi: {familiya.title()}")
toliq_ism('mokhirjons', 'khasanov')
# Foydalanuvchini ismi: Mokhirjons
# Foydalanuvchini familiyasi: Khasanov
toliq_ism('dilshod', 'nutfullayev')
# Foydalanuvchini ismi: Dilshod
# Foydalanuvchini familiyasi: Nutfullayev

# Yuqoridagi funksiya to'g'ri natija chiqarishi uchun argumentlarni ism va familiya ketma-ketligida kiritishimiz lozim.
# toliq_ism('olim','hakimov')
# Natija:
# Foydalanuvchi ismi: Olim
# Foydalanuvchi familiyasi: Hakimov
# Agar argumentlarni noto'g'ri ketma-ketlikda bersak, natija ham biz kutganday chiqmaydi:
# toliq_ism('hakimov','olim')
# Natija:
# Foydalanuvchi ismi: Hakimov
# Foydalanuvchi familiyasi: Olim
# Ko'p xolatlarda esa, argumentlarni noto'g'ri tartibda uzatish xatolikka ham olib kelishi mumkin.

def yosh_hisobla(ism, tugulgan_yil):
    """Foydalanuvchini yoshini hisoblovchi dastur"""
    print(f"{ism.title()} {2023 - tugulgan_yil} yoshda")
yosh_hisobla('mokhirjons', 1998)
# Mokhirjons 25 yoshda

# yosh_hisobla(1997, 'olim')
# Natija: AttributeError: 'int' object has no attribute 'title'

# KALIT SO'Z BILAN UZATISH
# Yuqoridagi kabi holatlarning oldini olish uchun argumentlarni parametr nomi bilan qo'shib uzatishimiz mumkin. Buning uchun funksiyaga o'zgartirish kiritish talab qilinmaydi.

yosh_hisobla(tugulgan_yil=1998, ism='mokhirjon')
# Mokhirjon 25 yoshda

# Yuoqirdagi misolda funksiyani chaqirishda biz parametrlar ketma-ketligiga rioya qilmagan bo'lsakda, argumentlarni parametr_nomi=qiymat ko'rinishida yozganimiz sababli funksiya to'g'ri ishladi.
# Huddi shu kabi yuqoridagi toliq_ism funksiyasiga murojat qilishimiz mumkin:

toliq_ism(familiya='khasanov', ism='mokhirjon')
# Foydalanuvchini ismi: Mokhirjon
# Foydalanuvchini familiyasi: Khasanov

# Kalit so'z usulidan foydalanganda parametr nomi to'g'ri yozilganiga ahamiyat bering.

# STANDART QIYMAT
# Funksiya yaratishda, istalgan parametr uchun standart qiymat ko'rsatib ketishimiz mumkin. Agar foydalanuvchi shu parametr uchun qiymat (argument) kiritmasa, funksiya bajarilishi jarayonida standart qiymat ishlatiladi. Standart qiymatni funksiya yaratish vaqtidaparametr = qiymat ko'rinishida beriladi.

def yosh_hisobla(tugulgan_yil, joriy_yil = 2023):  # joriy yil uchun qiymat 2023
    """Foydalanuvchi tug'ulgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil - tugulgan_yil} yoshdasiz.")
yosh_hisobla(1998)
# Siz 25 yoshdasiz.

# Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. Aks holda xatolik yuzaga keladi.

# Keling avval funksiyani ikkala argument bilan chaqiramiz:
# yosh_hisobla(1995,2020)
# Natija: Siz 25 yoshdasiz
# Endi esa faqat bitta argument (tugilgan_yil) bilan chaqiramiz:
# yosh_hisobla(1993)
# Natija: Siz 27 yoshdasiz
# Bu safar foydalanuvchi joriy_yil ni kiritmagani sababli, standart qiymat, 2020 ishlatildi.

# FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR
# Funksiyalarga murojat qilishda turli xatoliklarga yo'l qo'shimiz tabiiy. Bunday holatlarda Python qaytargan xatoni sinchiklab o'qib, xato qayerdaligini topishimiz va uni to'g'rilashimiz zarur. Quyida men avvalroq yaratgan funksiyalarimizni xato usullar bilan chaqiraman. Xato nimada ekanini topa olasizmi?

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)
# Natija: TypeError: unsupported operand type(s) for -: 'int' and 'str'
# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#
# yosh_hisobla(1993)
# Natija: TypeError: yosh_hisobla() missing 1 required positional argument: 'joriy_yil'
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
#
# salom_ber('hasan')
# Natija: TypeError: salom_ber() takes 0 positional arguments but 1 was given
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
#
#  toliq_ism('olim hakimov')
# Natija: TypeError: toliq_ism() missing 1 required positional argument: 'familiya'

# AMALIYOT

# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def tugulgan_yil(ism, familiya, tugulgan_yil, joriy_yil = 2023):
    """Tugulgan yilini hisoblaydigan funksiya"""
    print(f"{familiya.title()} {ism.title()} {joriy_yil - tugulgan_yil} da tug'ulgansiz")
tugulgan_yil('mokhirjo', 'khasanov', 1998)
# Khasanov Mokhirjo 25 da tug'ulgansiz

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def son_funk(son):
    """Sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2}, kubi esa {son**3}")
son_funk(2)
son_funk(3)
son_funk(4)
son_funk(5)
# 2 ning kvadrati 4, kubi esa 8
# 3 ning kvadrati 9, kubi esa 27
# 4 ning kvadrati 16, kubi esa 64
# 5 ning kvadrati 25, kubi esa 125

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def son_juft_toq(son):
    """Sonning juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son % 2 == 0:
        print(f"{son} - juft")
    else:
        print(f"{son} - toq")
son_juft_toq(4)
son_juft_toq(5)
son_juft_toq(6)
son_juft_toq(7)
# 4 - juft
# 5 - toq
# 6 - juft
# 7 - toq

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def sonlar_tengligi(son_1, son_2):
    """Sonlar tengligi uchun funksiya"""
    if son_1 > son_2:
        print(f"{son_1} > {son_2}")
    elif son_1 < son_2:
        print(f"{son_1} < {son_2}")
    else:
        print(f"Sonlar teng")
sonlar_tengligi(1, 2)
sonlar_tengligi(3, 4)
sonlar_tengligi(5, 6)
sonlar_tengligi(7,7)
sonlar_tengligi(9, 8)
# 1 < 2
# 3 < 4
# 5 < 6
# Sonlar teng
# 9 > 8

# Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.
def x_y(x, y):
    """xning y darajasi uchun funksiya"""
    print(f"{x} ning {y} darajasi {x**y}")
x_y(2, 3)
x_y(4, 5)
x_y(6, 7)
x_y(8, 9)
# 2 ning 3 darajasi 8
# 4 ning 5 darajasi 1024
# 6 ning 7 darajasi 279936
# 8 ning 9 darajasi 134217728

# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def x_2(x, y = 2):
    """x ning 2 - darajasi uchun funksiya"""
    print(f"{x} ning {y} darajasi {x**y} ga teng.")
x_2(2, 2)
x_2(3, 4)
x_2(4, 5)
x_2(5, 6)
# 2 ning 2 darajasi 4 ga teng.
# 3 ning 4 darajasi 81 ga teng.
# 4 ning 5 darajasi 1024 ga teng.
# 5 ning 6 darajasi 15625 ga teng.

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def son_qol(son):
    """ sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for i in range(2, 11):
        if not son % i:
            print(f"{son} {i} ga qoldiqsiz bo'linadi.")
son_qol(10)
son_qol(20)
son_qol(30)
son_qol(40)
son_qol(50)
# 10 2 ga qoldiqsiz bo'linadi.
# 10 5 ga qoldiqsiz bo'linadi.
# 10 10 ga qoldiqsiz bo'linadi.
# 20 2 ga qoldiqsiz bo'linadi.
# 20 4 ga qoldiqsiz bo'linadi.
# 20 5 ga qoldiqsiz bo'linadi.
# 20 10 ga qoldiqsiz bo'linadi.
# 30 2 ga qoldiqsiz bo'linadi.
# 30 3 ga qoldiqsiz bo'linadi.
# 30 5 ga qoldiqsiz bo'linadi.
# 30 6 ga qoldiqsiz bo'linadi.
# 30 10 ga qoldiqsiz bo'linadi.
# 40 2 ga qoldiqsiz bo'linadi.
# 40 4 ga qoldiqsiz bo'linadi.
# 40 5 ga qoldiqsiz bo'linadi.
# 40 8 ga qoldiqsiz bo'linadi.
# 40 10 ga qoldiqsiz bo'linadi.
# 50 2 ga qoldiqsiz bo'linadi.
# 50 5 ga qoldiqsiz bo'linadi.
# 50 10 ga qoldiqsiz bo'linadi.



