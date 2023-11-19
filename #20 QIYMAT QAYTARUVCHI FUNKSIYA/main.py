# #20 QIYMAT QAYTARUVCHI FUNKSIYA
#  Funksiyadan qiymat qaytarishni o'rganamiz

# Avvalgi darsimizda yaratgan barcha funksiyalarimiz konsolga ma'lumot chiqarayotgan edi. Aslida, aksar holatlarda bu g'ayritabiiy. Sababi, dasturchi sifatida biz konsolga chiqqan ma'lumotdan unumli foydalana olmaymiz. Konsoldagi qiymatni o'zgaruvchiga yuklab, undan kelajakda foydalanib ham bo'lmaydi. Mana shunday holatlarda, funksiyadan unumli foydalanish uchun undan biror qiymatni qaytarish maqsadga muvofiq bo'ladi.

# FUNKSIYADAN ODDIY QIYMAT QAYTARISH

# Keling ism va familiya degan parametrlarni olib, toliq_ism qaytaradigan sodda funksiya yasaymiz.

def toliq_ism_yasa(ism, familiya):
    """Toliq ismni qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism  # qiymat qaytarish uchun return operatorini ishlatamiz

# Yuqoridagi funksiyamizga ahamiyat bersangiz, uning badanida endi print() funksiyasi yo'q. Buning o'rniga, funksiyamiz return operatori yordamida toliq_ism degan o'zgaruvchining qiymatini qaytaradi.
# Endi funksiyadan to'g'ri foydalanish uchun u qaytargan qiymatni biror o'zgaruvchiga yuklashimiz kerak:

talaba1 = toliq_ism_yasa('mokhirjon', 'khasanov')
talaba2 = toliq_ism_yasa('dilshod', 'nutfullayev')

# Yuqoridagi kodlarni bajarganimizda konsolga hech narsa chiqmaydi. talaba1 va talaba2 o'zgaruvchilarining qiymatini ko'rish uchun esa print() funksiyasidan foydalanamiz.

print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")
# Darsga kelmagan talabalar: Mokhirjon Khasanov va Dilshod Nutfullayev

# Demak, qiymat qaytaradigan funksiyaning afzalligi shundaki, biz bu qiymatlardan keyin ham bemalol foydalanishimiz mumkin.

# Funksiya ichidagi o'zgaruvchilar mahalliy yoki ichki o'zgaruvchilar deyiladi (local variables). Ichki o'zgaruvchilar faqatgina funksiya ichida mavjud bo'ladi, ularga tashqaridan murojat qilib bo'lmaydi. Shuning uchun ham funksiya o'zgaruvchi emas qiymat qaytaradi.

# IXTIYORIY ARGUMENTLAR

# Avvalgi darsizmida funksiyalarga standart parametr berishni ko'rgan edik. Huddi shu usul bilan, ba'zi argumentlarni ixtiyoriy qilishimiz mumkin. Ya'ni funksiya ishlashi uchun bu agrumentarni kiritish majburiy emas, ixtiyoriy bo'ladi.

# Keling avvalgi funksiyamizni o'zgartiramiz va unga yana bitta otasiningismi degan paramter qo'shamiz, lekin bu parametr ixtiyoriy bo'ladi. Buning uchun funksiya yaratishda otasining_ismi='' deb yozib ketamiz.

def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
    """Toliq ismni qaytaruvchi funksiya"""
    if otasining_ismi:  # otasining ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
# Yuqoridagi funksiyani tahlil qiladigan bo'lsak, 3-qatorda biz otasiningismi parametri bo'sh yoki yo'qligini tekshiramiz. Pythonda if dan so'ng bo'sh bo'lmagan matn (string) yozsak, bu shart True qaytaradi. Demak, bu ixtiyoriy parametr kiritilgani yoki yo'qligiga qarab, funksiyamiz turlicha qiymat qaytaradi.

talaba1 = toliq_ism_yasa('mokhirjon', 'khasanov')  # otasining _ismi kiritilmadi
talaba2 = toliq_ism_yasa('dilshod', 'nutfullayev', 'doniyorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# Darsga kelmagan talabalar: Mokhirjon Khasanov va Dilshod Doniyorovich Nutfullayev

# FUNKSIYADAN LUG'AT QAYTARAMIZ

# Funksiyadan sodda qiymat emas, ro'yxat, lu'gat va boshqa ma'lumot turlarini ham qaytarishimiz mumkin.  Quyidagi funksiya ham mashina haqidagi ma'lumotlarni jamlab, ularni lug'at ko'rinishida qaytaradi:

def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {'kompaniya': kompaniya,
            'model': model,
            'rang': rangi,
            'korobka': korobka,
            'yil': yili,
            'narh': narhi}
    return avto

# E'tibor bering, narhi nomli parametrga None standart qiymatini berib ketdik. None Pythonda mavjud emas ma'nosini beradi, va if yordamida tekshirganda False mantiqiy qiymatini qaytardi.
# Quyidagi kodni tahlil qilishni sizga vazifa sifatida qoldiramiz:

avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', '2018')
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', '2016', '15000')
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
# Onlayn bozordagi mavjud avtomashinalar:
# Qora Malibu. Narhi: Noma'lum
# Oq Gentra. Narhi: 15000

# FUNKSIYADAN RO'YXAT QAYTARAMIZ

# Biz avvalroq range() funksiyasi bilan tanishgan edik. Bu funksiya 2 ta son qabul qilib, shu ikki son orali'g'idagi sonlarni qaytaradi. Keling biz oraliq() degan yangi funksiya yaratamiz. range() dan farqli ravishda, funksiyamiz 2 son oralig'idagi sonlarni ro'yxat ko'rinishida qaytarsin.

def oraliq(min, max):
    sonlar = []  # bo'sh ro'yxat
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar
# Funksiyani tekshiramiz:

print(oraliq(0, 10))
print(oraliq(10, 21))
print(oraliq(21, 11))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# []

# Yuqoridagi funksiyaga uchinchi, qadam deb nomlangan ixtiyoriy parameterni qo'sha olasizmi?

# print(oraliq(0,21,2)) # 0 dan 21 gacha 2 qadam bilan
# Natija: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# FUNKSIYALARNI TSIKLDA ISHLATISH

# Funksiyalarni takrorlash uchun tsikldan foydalanishimiz mumkin. Quyidagi misolda biz while yordamida avvalroq yaratgan avto_info funksiyamizni bir necha bor chaqiramiz va salondagi avtolar ro'yxatini shakllantiramiz. Bunda, ro'yxatning har bir elementi avto_info funksiyasidan qaytgan lug'at bo'ladi.
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end="\n")
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")


    # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == "no":
        break

# Yuqoridagi funksiyani Pythonda bajarib kor'ing. Ro'yxatga bir necha qiymatlar qo'shing. Natijalarni konsolga chiroyli qilib chiqaring:
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto["narh"]:
        narh = avto["narh"]
    else:
        narh = "Noma'lum"
    print(
        f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}"
    )
# Saytimizdagi avtolar ro'yxatini shakllantiramiz.
#
# Quyidagi ma'lumotlarni kiriting
# Ishlab chiqaruvchi: GM
# Modeli: Malibu
# Rangi: Qora
# Korobka: Avtomat
# Ishlab chiqarilgan yili: 2022
# Narhi: 35000
# Yana avto qo'shasizmi? (yes/no): yes
#
# Quyidagi ma'lumotlarni kiriting
# Ishlab chiqaruvchi: GM
# Modeli: Gentra
# Rangi: Oq
# Korobka: Mexanika
# Ishlab chiqarilgan yili: 2021
# Narhi: 15000
# Yana avto qo'shasizmi? (yes/no): no
#
# Salonimizdagi avtolar:
# Qora Malibu, Mexanika korobka. Narhi: 35000
# Oq Gentra, Mexanika korobka. Narhi: 15000

# AMALIYOT

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def malumotlar(ism, familiya, tugulgan_yil, tugulgan_joy, email_manzil, telefon_raqam):
    """Foydalanuvchini malumotlarini tuplovchi va konsolga chiqaruvchi funksiya"""
    foydalanuvchi = {
        "ism": ism,
        "familiya": familiya,
        "tugulgan_yil": tugulgan_yil,
        "yoshi": 2023 - tugulgan_yil,
        "tugulgan_joy": tugulgan_joy,
        "email_manzil": email_manzil,
        "telefon_raqam": telefon_raqam,
    }
    return foydalanuvchi

print("Foydalanuvchi haqida ma'lumotlarni kiriting.")
foydalanuvchilar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tugulgan_yil = int(input("Tug'ilgan yili: "))
    tugulgan_joy = input("Tug'ilgan joyi: ")
    email_manzil = input("Email: ")
    telefon_raqam = input("Telefon raqami: ")
    foydalanuvchilar.append(malumotlar(ism, familiya, tugulgan_yil, tugulgan_joy, email_manzil, telefon_raqam))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break

print("Foydalanuvchilar:")
for foydalanuvchi in foydalanuvchilar:
    print(
        f"{foydalanuvchi['ism'].title()} {foydalanuvchi['familiya'].title()} "
        f"{foydalanuvchi['yoshi']} yoshda, telefoni: {foydalanuvchi['telefon_raqam']}"
    )

# Foydalanuvchi haqida ma'lumotlarni kiriting.
# Ismi: mokhirjon
# Familiyasi: khasanov
# Tug'ilgan yili: 1998
# Tug'ilgan joyi: uchquduq
# Email: mokhirjons1@icloud.com
# Telefon raqami: +998909297161
# Davom etasizmi? (ha/yo'q)yo'q
# Foydalanuvchilar:
# Mokhirjon Khasanov 25 yoshda, telefoni: +998909297161

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def kattasi(x, y, z):
    """Uchta sonni eng kattasini qaytaruvchi funksiya"""
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max
print(kattasi(1, 2, 3))
print(kattasi(4, 5, 6))
print(kattasi(7, 8, 9))
# 3
# 6
# 9

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
def aylana_info(radius, pi = 3.14159):
    """aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * pi * radius,
        "yuzi": pi * radius**2
    }
    return aylana
print(aylana_info(2))
# {'radius': 2, 'diametr': 4, 'perimetr': 12.56636, 'yuzi': 12.56636}

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar
print(tub_sonlar_top(1, 11))
# [2, 3, 5, 7, 11]

# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
def fibonacci(n):
    """fibonachchi ketma-ketligi funksiyasi"""
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar

print(fibonacci(10))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
