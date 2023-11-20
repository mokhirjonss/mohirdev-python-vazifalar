# 21 FUNKSIYA VA RO'YXAT
# Funksiyaga ro'yxat uzatishni o'rganamiz

# FUNKSIYAGA RO'YXAT UZATISH
# Biz avvalgi darslarimizda funksiyaga parametr sifatida yagona qiymat berayotgan edik. Aslida, bu bilan cheklanmasdan, funksiyaga ro'yxat (list) ham berishimiz mumkin. Bunda, funksiya ro'yxat qiymatlariga to'g'ridan-to'g'ri murojat qila oladi.
# Keling talabalarni baholaydigan funksiya yozamiz. Funksiyamiz talabalar ro'yxatini qabul qilib oladi, ro'yxatdan har bir talabani sug'urib olib (.pop()), bahosini kiritishni so'raydi. Talaba ismi va bahosini lug'atga joylab, yakuniy lug'atni foydalanuvchiga qaytaradi.

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
# Talaba Husanning bahosini kiriting: 4
# Talaba Hasanning bahosini kiriting: 5
# Talaba Valining bahosini kiriting: 3
# Talaba Alining bahosini kiriting: 4
# {'husan': '4', 'hasan': '5', 'vali': '3', 'ali': '4'}

# RO'YXATGA O'ZGARTIRISH KIRITISH
# Funksiyaga ro'yxat uzatganimizda, funksiya ro'yxat elementlariga to'g'ridan-to'g'ri murojat qila oladi. Ro'yxatga funksiya ichida kiritilgan o'zgartirishlar asl ro'yxatga ham ta'sir qiladi. Avvalgi misolimizga qaytaylik:
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)

# Yuqoridagi funksiya unga uzatilgan ro'yxat ichidagi talabalarning ismini .pop() yordamida sug'urib olgani uchun bizning asl ro'yxatimiz ham bo'shab qoldi. E'tibor bering, funksiya tashqarisidagi va ichidagi ro'yxatlar ikki hil nomlangan bo'lsada (talabalar va ismlar), ikkalasi ham xotiradagi bitta ro'yxatga bog'langani sabab ulardan biriga o'zgartirish kiritilishi bilan, ikkinchisi ham o'zgaradi.

# ASL RO'YXATGA O'ZGARTIRISH KIRITISHNING OLDINI OLISH
# Agar funksiya asl ro'yxatga o'zgartirish kiritishini istamasangiz, funksiyaga ro'yxatning o'zini emas, uning nusxasini uzatish mumkin. Buning uchun funksiya parametrini royxat_nomi[:] ko'rinishida yozish kifoya. Bunda [:] operatori ro'yxatdan nusxa olishni bildiradi:
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)
# Natija: ['ali', 'vali', 'hasan', 'husan']

# AMALIYOT

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
# ['Ali', 'Vali', 'Hasan', 'Husan']

# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
# ['ali', 'vali', 'hasan', 'husan']
# ['Ali', 'Vali', 'Hasan', 'Husan']

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
# Talaba Alining bahosini kiriting: 3
# Talaba Valining bahosini kiriting: 4
# Talaba Hasanning bahosini kiriting: 5
# Talaba Husanning bahosini kiriting: 6
# {'ali': '3', 'vali': '4', 'hasan': '5', 'husan': '6'}
# ['ali', 'vali', 'hasan', 'husan']
