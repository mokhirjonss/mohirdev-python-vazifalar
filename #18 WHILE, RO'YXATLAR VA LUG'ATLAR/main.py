# 18 WHILE, RO'YXATLAR VA LUG'ATLAR
# While tsikli yordamida ro'yxatlar bilan ishlashni o'rganamiz.

# Ro'yxatlar (lug'atlar) bilan ishlashda while tisklining foydalari juda ko'p. Misol uchun foydalanuvchidan bir nechta ma'lumotlarni qabul qilib olish, ro'yxatdan takrorlanuvchi qiymatlarni o'chirib tashlash yoki bir ro'yxatni ikkinchi ro'yxatga ko'chirishda while tsiklidan foydalanishimiz mumkin.

# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

# Quyidagi dasturga e'tibor bering, avval ismlar degan bo'sh ro'yxat yaratib oldik. Keyin esa while tsikli yordamida foydalanuvchidan ro'yxatga ism qo'shishni so'raymiz. So'ngra foydalanuvchidan yana ism qo'shmoqchi yoki yo'q ekanin so'raymiz va foydalanuvchining javobiga ko'ra yoki while ni boshiga qaytamiz, yoki tsiklni to'xtatamiz.

ismlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n = 1  # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n} - do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
    if javob == 'ha':
        n += 1
        continue
    else:
        break

print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
# Yaqin do'stlaringiz ro'yxatini tuzamiz.
# 1 - do'stingiz ismini kiriting: mokhirjon
# Yana ism qo'shasizmi? (ha/yo'q) ha
# 2 - do'stingiz ismini kiriting: dilshod
# Yana ism qo'shasizmi? (ha/yo'q) yo'q
# Do'stlaringiz ro'yxati:
# Mokhirjon
# Dilshod

# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH
# Yuqoridagi usul bilan lu'gatlarni ham shakllantirishimiz mumkin. Quyidagi kodda ism bu kalit, yosh esa klaitga mos keluvchi qiymat. while tsiklining davomiyligi esa ishora ning qiymatiga bog'liq.

print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()} yoshini kiriting: ")
    dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat

    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda.")

# Do'stlaringiz yoshini saqlaymiz.
# Do'stingiz ismini kiriting: mokhir
# Mokhir yoshini kiriting: 25
# Yana ma'lumot qo'shasizmi? (ha/yo'q)ha
# Do'stingiz ismini kiriting: dilshod
# Dilshod yoshini kiriting: 24
# Yana ma'lumot qo'shasizmi? (ha/yo'q)yo'q
# Mokhir 25 yoshda.
# Dilshod 24 yoshda.

# RO'YXAT ELEMENTLARINI O'CHIRISH
# Avvalgi darslarimizning birida ro'yxat elementini o'chirish uchun .remove(qiymat) metodi bilan tanishgan edik. Esingizda bo'lsa, bu metod ro'yxatdan eng birinchi uchragan qiymatni o'chiradi. Agar ro'yxatimizda ma'lum bir qiymat bir necha bor takrorlangan bo'lsa, ularning barchasini o'chirib tashlash uchun while tsiklidan foydalanishmiz mumkin.

cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
while 'nexia' in cars:  # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia')  # nexia ni ro'yxatdan olib tashla
print(cars)
# ['lacetti', 'toyota', 'audi', 'malibu']

# Yuqoridagi tsikl toki cars degan ro'yxatda 'nexia' qiymati tugagunga qadar takrorlanaveradi.

# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
# Tasavvur qiling bizda ma'lum bir ro'yxat bor, biz ro'yxatdagi har bir element ustida biror amalni bajarib, uni birinchi ro'yxatdan ikkinchi ro'yxatga ko'chirib olmoqchimiz. Shunday holatlarda while tsikli juda qo'l keladi.
# Quyidagi misolni ko'raylik. Bizda talabalar ro'yxati bor. while tsikli toki ro'yxatda talabalar bor ekan aylanaveradi. Tsikl ichida biz .pop() metodi yordamida talabaning ismini ro'yxatdan sug'urib oldik va foydalanuvchidan talabani baholashni so'radik. Talabaning ismi va bahosini lug'at elementi ko'rinishida saqlab qo'ydik (talaba - kalit, baho - qiymat).

talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba] = int(baho)
# Botirning bahosini kiriting: 4
# Botir baholandi.
# Olimning bahosini kiriting: 5
# Olim baholandi.
# Husanning bahosini kiriting: 3
# Husan baholandi.
# Hasanning bahosini kiriting: 5
# Hasan baholandi.

# Yuqorida biz while tsikli yordamida ro'yxat va lug'atlar ustida bajarish mumkin bo'lgan ba'zi misollarni ko'rdik. Albatta dasturlash davomida bundan boshqa holatlar ham uchrashi tabiiy.

# AMALIYOT

# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

savat = []
while True:
    mahsulot = input(f"Savatga mahsulot qo'shing: ")
    savat.append(mahsulot)
    javob = input(f"Yana mahsulot qo'shasizmi? (ha/yo'q)")
    if javob != "ha":
        break
print("Dastur tugadi!")
print(savat)
# Savatga mahsulot qo'shing: olma
# Yana mahsulot qo'shasizmi? (ha/yo'q)ha
# Savatga mahsulot qo'shing: olcha
# Yana mahsulot qo'shasizmi? (ha/yo'q)ha
# Savatga mahsulot qo'shing: banan
# Yana mahsulot qo'shasizmi? (ha/yo'q)yo'q
# Dastur tugadi!
# ['olma', 'olcha', 'banan']

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
mahsulotlar = {}
while True:
    mahsulot = input(f"Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = int(narh)
    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    if javob != "ha":
        break
print("Mahsulotlar qo'shildi")
print(mahsulotlar)
# Mahsulot nomini kiriting: olma
# Olmaning narhini kiriting: 5000
# Yana mahsulot qo'shasizmi? (ha/yo'q)ha
# Mahsulot nomini kiriting: olcha
# Olchaning narhini kiriting: 4000
# Yana mahsulot qo'shasizmi? (ha/yo'q)ha
# Mahsulot nomini kiriting: banan
# Bananning narhini kiriting: 6000
# Yana mahsulot qo'shasizmi? (ha/yo'q)yo'q
# Mahsulotlar qo'shildi
# {'olma': 5000, 'olcha': 4000, 'banan': 6000}

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
# Bizda qovun yo'q
# Uzum - 22000 so'm
# Bizda anjir yo'q
# Olma - 20000 so'm


