# #17 WHILE TSIKLI
# while tsikli bilan tanishamiz

# YANA input()
# Dasturlar foydalanuvchining muammolarini hal qilish uchun yoziladi. Buning uchun esa, foydalanuvchi bilan aloqa o'rnatish, undan turli ma'lumotlarni qabul qilib olib talab etiladi. Misol uchun, dasturimiz foydalanuvchiga ismi bilan murojat qilishi uchun, avval uning ismini so'rashi kerak. Yoki, foydalanuvchi istagan ma'lumotni topish uchun avval undan biror kalit so'z kiritishni so'rash kerak va hokazo.
# Biz avvalgi darsimizda input() yordamida foydalanuvchidan qiymat qilishni o'rgangan edik. Dastur davomida input() funktsiyasini chaqirganimizda dastur foydalanuvchi biror matn kiritiib, Enter tugmasini bosgunga qadar to'xtab turadi.
# Foydalanuvchi kiritgan qiymatni biror o'zgaruvchiga yuklash, va undan dastur davomida foydalanish mumkin.

ism = input("Ismingiz nima? ")
print(f'Salom, {ism.title()}')
# Ismingiz nima? mokhirjons
# Salom, Mokhirjons

# input() finktsiyasi ichidagi matn ingliz tilida prompt, savol deyiladi. Aslida biz savolni ham o'zgaruvchiga yuklab, shaxsiy so'rovnomalar ham yaratishimiz mumkin.

ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
print(f"{yosh} ga kiribsiz qachon endi uylanasiz a {ism.title()}")
# Ismingiz nima? mokhirjons
# Salom, Mokhirjons. Yoshingiz nechida? 25
# 25 ga kiribsiz qachon endi uylanasiz a Mokhirjons

# Yuqorida birinchi input() bilan foydalanuvchi ismini so'radik va yangi savol matnini yasab oldik.

# Sonlar va input()
# input() funktsiyasi har qanday kiritilgan qiymatni matn sifatida qabul qilib oladi. Agar foydalanuvchidan son talab qilinsa, foydalanuvchi kiritgan qiymatni butun (integer) yoki on'lik (float) son ko'rinishiga o'tkazib olish kerak.
# Buning uchun int() yoki float() funktsiyalaridan foydalanamiz.

ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
yosh = int(yosh)  # yosh ni butun songa o'tkazamiz
height = input("Bo'yingiz necha metr? ")
height = float(height) # bo'yni o'nli songa o'tqazamiz
print(f"{ism.title()} aka {yosh} ga kirib bo'yiz {height}sm mi?")
# Ismingiz nima? mokhirjons
# Salom, Mokhirjons. Yoshingiz nechida? 25
# Bo'yingiz necha metr? 180
# Mokhirjons aka 25 ga kirib bo'yiz 180.0sm mi?

# Foydalanuvchidan qiymat so'raganingizda input()ichidagi savolni aniq va tushunarli qilib yozing. Masalan: input("Tug'ilgan yilingizni kiriting: ")

# while TSIKLI BILAN TANISHAMIZ
# Biz avvalroq for tsikli bilan tanishgan edik. for tsikli ma'lum bir ro'yxatni olib, ro'yxat ichidagi qiymatlar tugaginga qadar biror kodni takrorlar edi. while ham takrorlash operatori bo'lib, for dan farqli ravishda, toki ma'lum bir shart to'g'ri (True) bo'lsa, kodni takrorlayveradi.

# while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.

# Keling sodda misol ko'ramiz, while yordamida 5 gacha sanaymiz:

son = 1  # son ga 1 qiymatini beramiz
while son <= 5:  # toki son 5 dan kichik yoki teng ekan
    print(son, end=' ')  # son ni konsolga chiqaramiz
    son = son + 1
# 1 2 3 4 5

# Yuqoridagi kodni tahlil qilamiz:
# avval son degan o'zgaruvchi yaratdik va unga 1 qiymatini berdik.
# 2-qatorda esa toki son 5 dan kichik yoki teng ekan 3-4-qatorlarni bajar dedik.
# 3-qatorda son ni konsolga chiqardik
# 4-qatorda son ga 1 qo'shdik.
# 4-qatordan so'ng kod yana 2-qatorga qaytadi va son<=5 shartini tekshiradi, agar shart bajarilsa 3-4 qator qayta-qayta bajarilaveradi.
# 5-qadamdan so'ng son=5 bo'lganda while tsikli to'xtaydi.

# Pythonda += operatori bor. Bu operator o'ng tarafdagi qiymatni chap tarafdagi qiymatga qo'shadi. Misol uchun, yuqorida son = son + 1 o'rniga son += 1 deb yozishimiz mumkin.

# while va input()
# Shu paytgacha yozgan dasturlarimiz faqatgina bir martta bajarilayotgan edi. while tsikli yordamida dasturni to'xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.

print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
# Kiritilgan sonning kvadratini qaytaruvchi dastur
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 125
# 15625.0
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 6
# 36.0
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): exit

# Yuoqridagi dasturimiz toki foydalanuvchi exit deb yozguniga qadar takrorlanaveradi.

# Ishora (flag)
# Yuqoridagi dasturda dasturni to'xtatish uchun yagona shartni tekshirdik (qiymat!='exit'), katta dasturlarda bir emas bir nechta shartlarni tekshirish, va ulardan biri bajarilgan taqdirda dasturni to'xtatish talab qilinishi mumkin.
# Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz mumkin. Agar dastur bajarilishi davomida dasturni to'xtatish shartlaridan biri bajarilganda ishora o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi.

print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
# Kiritilgan sonning kvadratini qaytaruvchi dastur
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 3
# 9.0
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 4
# 16.0
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): exit

# BREAK OPERATORI
# Break operatori yordamida ma'lum bir shartni tekshirish va while tsikli bajarilishini to'xtatib qo'yish mumkin.

print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**2)
# Kiritilgan sonning kvadratini qaytaruvchi dastur
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 2
# 4.0
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 5
# 25.0
# Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): exit

# Break operatori for tsiklini to'xtatish uchun ham ishlatiladi.

sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:  # son 5 ga teng bo'lsa kod to'xtaydi.
        break
    print(f"{son} ning kvadrati {son**2} ga teng.")
# 1 ning kvadrati 1 ga teng.
# 2 ning kvadrati 4 ga teng.
# 3 ning kvadrati 9 ga teng.
# 4 ning kvadrati 16 ga teng.

# while tsikli ichida bir nechta break operatori ham bo'lishi mumkin.

# CONTINUE OPERATORI
# Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljallangan.

sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tsikl boshiga qaytadi.
        continue
    print(f"{son} ning kvadrati {son**2} ga teng.")
# 1 ning kvadrati 1 ga teng.
# 2 ning kvadrati 4 ga teng.
# 3 ning kvadrati 9 ga teng.
# 4 ning kvadrati 16 ga teng.
# 6 ning kvadrati 36 ga teng.
# 7 ning kvadrati 49 ga teng.
# 8 ning kvadrati 64 ga teng.
# 9 ning kvadrati 81 ga teng.
# 10 ning kvadrati 100 ga teng.

son = 0
while son < 10:
    son += 1
    if son % 2 != 0:
        continue
    else:
        print(son)
# 2
# 4
# 6
# 8
# 10

# while tsikli ichida bir nechta continue operatori ham bo'lishi mumkin.

# ABADIY TSIKL TUZOG'I
# Tsikllar bilan ishlashda abadiy tsikl yaratib qo'yishdan ehtiyot bo'lishimiz kerak. Abadiy tsiklga turli mantiqiy xatolar sabab bo'lishi mumkin: noto'g'ri shart, o'zgarmas qiymat, kodlar ketma-ketligida xatolik va hokazo.
# Kelin ba'zi misollarni ko'ramiz:

# infinite loop
son = 0
while son < 10:
    if son % 2 != 0:
        continue
    else:
        print(son)
# 0
# 0
# 0
# 0
# 0
# 0

# Yuqoridagi kod abadiy davom etadi, sababi biz son ning qiymatini o'zgartirishni esdan chiqardik

son = 0
while son < 10:
    if son % 2 != 0:
        continue
    else:
        print(son)
    son += 1
# 0

# Bu kod ham abadiy davom etadi, lekin nima uchun?

son = 1
while son > 0:
    son += 1
    if son % 2 != 0:
        continue
    else:
        print(son)
# 2
# 4
# 6
# 8
# 10
# 12

# Yuqoridagi kodda esa xato shart tufayli (son>0) kod abadiy aylanadi.

# Dastur bajarilishini to'xtatish uchun konsolda Ctrl+C tugmasini bosing

# AMALIYOT

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
print("Yaxshi ko'rgan kitoblar uchun dastur")
savol = "Yaxshi ko'rgan kitobingizni yozing: "
savol += "(barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): "
while True:
    javob = input(savol)
    if javob == 'stop':
        break
    else:
        print("Rahmat!")
# Yaxshi ko'rgan kitobingizni yozing: (barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): python
# Rahmat!
# Yaxshi ko'rgan kitobingizni yozing: (barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): java
# Rahmat!
# Yaxshi ko'rgan kitobingizni yozing: (barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): stop

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

savol = "Yoshingiz nechida? "
savol += "(chiqish uchun 'exit' yoki 'quit' deb yozing): "
while True:
    javob = input(savol)
    if javob == 'exit' or javob == 'quit':
        break
    else:
        if int(javob) <= 7:
            print(f"Chipta narhi 2000 so'm")
        elif 7 < int(javob) <= 18:
            print(f"Chipta narhi 3000 so'm")
        elif 18 < int(javob) < 65:
            print(f"Chipta narhi 10000 so'm")
        else:
            print(f"Bepul")
# Yoshingiz nechida? (chiqish uchun 'exit' yoki 'quit' deb yozing): 25
# Chipta narhi 10000 so'm
# Yoshingiz nechida? (chiqish uchun 'exit' yoki 'quit' deb yozing): 64
# Chipta narhi 10000 so'm
# Yoshingiz nechida? (chiqish uchun 'exit' yoki 'quit' deb yozing): 6
# Chipta narhi 2000 so'm
# Yoshingiz nechida? (chiqish uchun 'exit' yoki 'quit' deb yozing): 66
# Bepul
# Yoshingiz nechida? (chiqish uchun 'exit' yoki 'quit' deb yozing): quit

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif int(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{int(qiymat)} ning ildizi {ildiz} ga teng.")
# Kiritilgan sonning ildizini qaytaruvchi dastur.
# Musbat son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 4
# 4 ning ildizi 2.0 ga teng.
# Kiritilgan sonning ildizini qaytaruvchi dastur.
# Musbat son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 16
# 16 ning ildizi 4.0 ga teng.
# Kiritilgan sonning ildizini qaytaruvchi dastur.
# Musbat son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): exit