#22 MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)
# *args va **kwargs bilan tanishamiz

# MOSLASHUVCHAN FUNKSIYA
# Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar sonini aniq bilmasangiz, Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyati bor.

# *args USULI
# Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona qiymatlar ko'rinishida uzatilsa, funksiya yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments).

# Quyidagi misolni ko'raylik. summa() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi, va ularning yi'gindisi hisoblaydi:

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

# Bu funksiyani istalgancha parametr bilan chaqirish mumkin:

print(summa(1, 2))
# 3

print(summa(1, 2, 3, 4, 5))
# 15

# *args usulida, bacha uzatilgan parametrlar (bir dona bo'lsa ham) funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi. Bundan kelib chiqib, yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisin hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4, 5, 6, 7))
# 22

# Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi:
def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
    return x + y + sum(sonlar)

# Yuqoridagi funksiyamiz kamida 2 ta parametr qabul qiladi (x va y) va birinchi ikki argumentlar majburiy argumentlardir.
print(summa(2, 3, 4, 5, 6, 7))
# 27

# print(summa(2))
# Netija: TypeError: summa() missing 1 required positional argument: 'y'

# **kwargs USULI
# Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa, va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).

# **kwargs — keyword arguments (kalit so'zli argumentlar)

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

#     return malumotlar
# Yuqoridagi funksiyamiz kompaniya va model degan ikki qiymatni qabul qiladi, undan keyin esa funksiyaga istalgancha parametr uzatish mumkin.  Bunday funksiyaga parametrlar kalitso'z=qiymat ko'rinishida uzatiladi.
# Funksiya ichida avval foydalanuvchi kiritgan qo'shimcha qiymatlardan iborat malumotlar deb nomlangan lug'at shakllantiriladi. Undan keyin esa majburiy parametrlarni lug'atga qo'shamiz.

avto1 = avto_info("GM", "malibu", rang = "qora", yil = 2018)
avto2 = avto_info("Kia", "K5", rang = "qizil", narh = 35000)
print(avto1, avto2)

# AMALIYOT

# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kupaytma(*sonlar):
    javob = 1
    for son in sonlar:
        javob *= son
    return javob
print(kupaytma(1, 2, 3))
# 6
print(kupaytma(4, 5, 6))
# 120
print(kupaytma(7, 8, 9))
# 504

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba1 = talaba_info("Mokhirjon", "Khasanov", yosh = 25, kurs = 4, fakultet = "IT")
talaba2 = talaba_info("Dilshod", "Nutfullayev", yosh = 24, kurs = 4, fakultet = "Mexanika")
print(talaba1)
print(talaba2)
# {'yosh': 25, 'kurs': 4, 'fakultet': 'IT', 'ism': 'Mokhirjon', 'familiya': 'Khasanov'}
# {'yosh': 24, 'kurs': 4, 'fakultet': 'Mexanika', 'ism': 'Dilshod', 'familiya': 'Nutfullayev'}
