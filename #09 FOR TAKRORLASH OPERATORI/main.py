# #09 FOR TAKRORLASH OPERATORI
# FOR operatori bilan ishlashni o'rganamiz

# for BILAN TANISHAMIZ
# Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo.
# Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi.
# Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(mehmon)
# Ali
# Vali
# Hasan
# Husan
# Olim

# Keling, kodni tahlil qilaylik.
# 1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.
# 2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib uni yangi, mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin. Biz tushunarli bo'lishi uchun mehmon deb atadik)
# 3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik. Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
# "For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.
# Yuqoridagi kodni oddiy tilga tarjima qilsak "Mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi.
# for QANDAY ISHLAYDI
# Keling yana bir misol ko'raylik.

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")
# Hurmatli Ali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmat bilan, Palonchiyevlar oilasi
# Hurmatli Vali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmat bilan, Palonchiyevlar oilasi
# Hurmatli Hasan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmat bilan, Palonchiyevlar oilasi
# Hurmatli Husan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmat bilan, Palonchiyevlar oilasi
# Hurmatli Olim, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmat bilan, Palonchiyevlar oilasi

# Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi. Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.
# Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi qismi asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. Agar biz mana shu surilishni tark qilsak kodimiz xato beradi:

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")
# Natija: IndentationError: expected an indented block
# Ko'rib turganingizdek for dan keyingi qatorni o'ngga surmaganimiz uchun indentation error (surishda xatolik) degan xabarni oldik.
# Shunigdek, ko'pchilik yo'l qo'yadigan yana bir xato, qo'shimcha qatorlarni surish esdan chiqishi:

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
print("Hurmat bilan, Palonchiyevlar oilasi\n")
# Hurmatli Ali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmatli Vali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmatli Hasan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmatli Husan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmatli Olim, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
# Hurmat bilan, Palonchiyevlar oilasi

# Yuqoridagi kodimizda 4-qatorni o'ngga surmaganimiz uchun, Python bu qatorni tsikl tashqarisida deb qabul qildi va faqatgina 1 marta, tsikl tugaganidan so'ng bajardi.
# Huddi shu kabi agar takrorlanishi kerak bo'magan kodni tsikldan so'ng o'ngga surib qo'ysak Python bu qatorni tsiklning tarkibida deb hisoblab, qayta-qayta bajaradi:

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(mehmon)

    print(mehmonlar)  # bu qator tsikl tashqarisida bo'lishi kerak edi
# Ali
# ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# Vali
# ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# Hasan
# ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# Husan
# ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# Olim
# ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# Yuoqirdagi misolda 5-qator o'ngga surilib qolgani uchun Python bu qatorni ham bir necha bor takrorlab, konsolga chiqardi. To'g'ri kod quyidagicha bo'ladi:

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(mehmon)

print(mehmonlar)
# Ali
# Vali
# Hasan
# Husan
# Olim
# ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
# Keling quyidagi misolni ko'ramiz

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
# 1 ning kvadrati 1 ga teng
# 2 ning kvadrati 4 ga teng
# 3 ning kvadrati 9 ga teng
# 4 ning kvadrati 16 ga teng
# 5 ning kvadrati 25 ga teng
# 6 ning kvadrati 36 ga teng
# 7 ning kvadrati 49 ga teng
# 8 ning kvadrati 64 ga teng
# 9 ning kvadrati 81 ga teng
# 10 ning kvadrati 100 ga teng

# for yordamida yangi ro'yxat ham shakllantirish mumkin:

sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for va input()
# for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:

dostlar = []  # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):  # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)
# 1-do'stingizning ismini kiriting: mokhirjons
# 2-do'stingizning ismini kiriting: dilshod
# 3-do'stingizning ismini kiriting: sherzod
# 4-do'stingizning ismini kiriting: timur
# 5-do'stingizning ismini kiriting: javohir
# ['mokhirjons', 'dilshod', 'sherzod', 'timur', 'javohir']

# Kodni tahlil qilamiz:
# 1-qatorda bo'sh dostlar ro'yxatini yaratdik
# 2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik
# 3-qatorda tsiklni boshladik. range(5) funktsiyasi 0 dan 5 gacha sonlar ketma-ketligini yaratadi (0,1,2,3,4) tsikl esa n shularning har biriga teng bo'lib chiqquncha davom etadi.
# 4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni kiriting deb so'radik. Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha qiymatlarni oladi, foydalanuvchiga tushunarli bo'lishi uchun esa biz "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting deb murojat qilyapmiz.
# 5-qatorda shakllangan ro'yxatni konsolga chiqardik.

# for tsikli har qanday dasturlash tilining eng muhim qismlaridan hisoblanadi va biz bu operatoraga hali takror-takror qaytamiz.

# AMALIYOT
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

ismlar = ['ali', 'vali', 'hasan', 'husan', 'olim']
for i in ismlar:
    print(f'Salom {i.title()}')
print(f'Kod {len(ismlar)} marta takrorlandi')
# Salom Ali
# Salom Vali
# Salom Hasan
# Salom Husan
# Salom Olim
# Kod 5 marta takrorlandi

for i in range(10, 101):
    if i % 2 != 0:
        print(i**3)
# 1331
# 2197
# 3375
# 4913
# 6859
# 9261
# 12167

kinolar = []
for i in range(5):
    kinolar.append(input(f'{i + 1} - kino: '))
print(kinolar)
# 1 - kino: shrek
# 2 - kino: up
# 3 - kino: volt
# 4 - kino: cars
# 5 - kino: lion king
# ['shrek', 'up', 'volt', 'cars', 'lion king']

odam = []
for i in range(int(input(f'Bugun necha kishi bn suhbat qildingiz? '))):
    odam.append(input(f'{i + 1} - suhbat qilgan odamingiz kim edi: '))
print(odam)
# Bugun necha kishi bn suhbat qildingiz? 3
# 1 - suhbat qilgan odamingiz kim edi: mokhirjons
# 2 - suhbat qilgan odamingiz kim edi: sherzod
# 3 - suhbat qilgan odamingiz kim edi: dilshod
# ['mokhirjons', 'sherzod', 'dilshod']