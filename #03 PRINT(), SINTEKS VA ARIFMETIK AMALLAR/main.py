# #03 PRINT(), SINTEKS VA ARIFMETIK AMALLAR
# print() funktsiyasi, Python sintaksi va arifmetik amallar
# PRINT()
# Avvalgi darsimizning yakunida bir nechta kodlarni pythonda bajarib ko'rishni vazifa qilgan edik. Keling shu kodlarning natijasini ko'ramiz:

print("Assalom alaykum")
# Assalom alaykum

# Kutilganidek, yuqoridagi kod Assalom alaykum matnini konsolda ko'rsatdi. Keling endi keyingi kodni kiritamiz:

print('Hayrli tong!') # нотугри ёзилиши керак аслида!

# Natija: SyntaxError: invalid syntax
# Bu safar esa Hayrli tong! yozuvi o'rniga, Syntax Error (sinteksda xatolik) xabari chiqdi. Xatolik qayerda?
# Avval aytganimizdek, print() funktsiyasi matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi. Lekin bu funktsiya to'g'ri ishlashi uchun bir nechta qoidalarga amal qilish lozim. Jumladan, agar konsolga matn chiqarmoqchi bo'lsak, matnimiz albatta qo'shtirnoq yoki (" ") yoki birtirnoq(' ') orasida yozlishi kerak. Demak Hayrli tong! so'zini konsolda chiqarish uchun to'g'ri kod:

print("Hayrli tong!")
# Hayrli tong!

# yoki

print('Hayrli tong!')
# Hayrli tong!

# Qo'shitrnoq yoki birtirnoq ishlatishning afzalliklaridan biri, agar siz chiqarmoqchi bo'lgan matnda ikkovidan biri qatnashgan bo'lsa, print() funktsyasida ikkinchisidan foydalanasiz. Keling quyidagi misolni ko'ramiz:

print('Men "Dell" markasidagi noutbuk sotib oldim')
# Men "Dell" markasidagi noutbuk sotib oldim

# Yuqoridagi matnda "Dell" so'zi qo'shtirnoq ichida eda. Bu matnni konsolga chiqarish uchun esa, print()funktsyasi ichida matnni birtirnoq ichiga oldik.
# Agar matnni bir necha qatorga bo'lib yozish talab qilinsa, uchtalik qo'shtirnoq(""" """)yoki birtirnoqdan (''' ''')foydalanish mumkin:

print("""Odami ersang, demagil odami,
Oniki, yo'q xalq g'amidin g'ami""")
# Odami ersang, demagil odami,
# Oniki, yo'q xalq g'amidin g'ami

# Qatorga bo'lishning yana bir usuli, qator so'nggida \n belgisini qo'yish.

print("Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami")
# Odami ersang, demagil odami,
# Oniki, yo'q xalq g'amidin g'ami

# Yuoqridagi matnni birtirnoq orqali ham konsolga chiqarish mumkinmi? Matndagi yo'q, g'am so'zlaridagi birtirnoqlar bunga to'sqinlik qilmaydimi? Qiladi.
# Buning oldini olish uchun esa matndagi birtirnoq belgisidan avval \ belgisini qo'yish lozim.

print('Odami ersang, demagil odami, \nOniki, yo\'q xalq g\'amidin g\'ami')
# Odami ersang, demagil odami,
# Oniki, yo'q xalq g'amidin g'ami

# SINTEKS XATOLIK (SYNTAX ERROR)
# Har bir tilda orfografik va grammatik qoidalar bo'lgani kabi, dasturlash tillarining ham o'ziga yarasha qonun-qoidalari bor. Bu qoidalar to'plami sinteks (syntax) deb ataladi. Sinteks xatolik (Syntax Error) deb esa shu qoidalarning buzilishiga aytiladi.
# Misol uchun keraksiz joyda qo'yilgan nuqta, vergul yoki bo'sh joy, shuningdek ma'lum funktsiyalar nomini xato yozish (print() o'rniga prit()), ochilmay yoki yopilmay qolgan qavs, noo'rin bo'shliq, qolib ketgan kalit so'z (keyword) kabilar ham Syntax Error hisoblanadi.
# Syntax Error eng ko'p uchraydigan xatolik bo'lib, Python bunday xatolik bor dasturlarni bajarmaydi.
# Biz darslarimiz davomida turli sinteks qoidalar haqida o'z o'rnida yana to'xtalamiz.

# ARIFMETIK AMALLAR
# Amaliyotga qaytamiz, print() funktsiyasi nafaqat matn, balki turli ifodalarni ham konsolga chiqaradi.
# Keling quyidagi kodlarni ham bajaramiz:

print(2 + 4 * 2)
# 10

# Python arifmetik amallarni bajarishda Matematika qoidalariga amal qiladi:
# Qavs ichidagi amallar qavs ortidagilardan avval bajariladi
# Darajaga oshirish (ildiz chiqarish) ko'paytirish va bo'lishdan avval bajariladi
# Ko'paytirish va bo'lish, qo'shish va ayirishdan avval bajariladi
# Boshqa holatlarda ifodalar chapdan o'ngga qarab bajariladi
# Yuqoridagi misolda ham avval ko'paytirish (4*2=8), keyin esa qo'shish amali (2+8=10) bajarildi.

print(19 / 5)
# 3.8

# Ko'rib turganingizdek, / belgisi bo'lish amalini bajaradi va natija har doim o'nlik son ko'rinishida bo'ladi (agarchi bo'lish amali natijasida butun son xosil bo'lsa ham):

print(20 / 5)
# 4.0

# Bo'lish amalidan butun son ko'rinishidagi natija olish uchun // belgisidan foydalanamiz:

print(16 // 4)
# 4

print(10 // 3)
# 3

# Amaliyotimizdagi keyingi kodni ham bajaraylik:

print(2**4)
# 16

# Yuqoridagi ** belgisi darajaga oshirishni anglatadi, ya'ni 2**4 ifodasi 2 ning 4-darajasini beradi.
# print() yordamida matn va ifodalarni jamlab chiqarish ham mumkin. Buning uchun har bir ifoda va matn vergul (,) bilan ajratiladi:

print("To'qqizning kvadrati", 9**2, "ga teng")
# To'qqizning kvadrati 81 ga teng

print('3 x 3 =', 3 * 3)
# 3 x 3 = 9

# IZOHLAR (COMMENTS)
# Yaxshi dasturchilarning odatlaridan biri har qanday kodni izohlar bilan tushuntirib ketish. Izohlar kelajakda o'zimiz uchun ham, boshqalar uchun ham dasturimiz qanday ishlashini tushunishda yordam beradi.
# Quyidagi ikki misolga e'tibor bering, va ulardan qay biri tushunarliroq ekanini solishtiring

print(2 * 5 * 3.14159)
# 31.4159

# #Radiusi 5 ga teng bo'lgan aylananing uzunligi quyidagicha hisoblanadi
# print(2*5*3.14159)

# Yuqoridagi misolda # belgisidan keyin yozilgan matn izoh (comment) deyiladi.
# Izoh alohida qatorda yoki qator oxiridan ham yozilishi mumkin. Python # dan keyingi har qanday matnni (qator oxirigacha) e'tiborsiz qoldiaradi. # dan keyin yozligan kodlar ham bajarilmaydi:

# print("Assalom alaykum!") # Bu matn konsolda chiqadi
# #Keyingi qator esa bajarilmaydi
# #print("Mening ismim Anvar")

# AMALIYOT
# Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
# "Nexia", "Tico", 'Damas' ko'rganlar qilar havas

print('"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas')
# "Nexia", "Tico", 'Damas' ko'rganlar qilar havas

# Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
# 5 ning 4-darajasini toping
# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
# Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
# Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( deb oling)
# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)

print(5**4)
# 625
print(22 % 4)
# 2
print(f'kvadratning yuzi: S = {125 * 125}, kvadratning perimetri: P = {2 * (125 + 125)} ')
# kvadratning yuzi: S = 15625, kvadratning perimetri: P = 500
print(f'doiraning yuzi: S = {3.14 * (6**2)}')
# doiraning yuzi: S = 113.04
print(f'to\'g\'ri burchakli uchburchakning gipotenuzasi: c = {(6**2 + 7**2)**0.5}')
# to'g'ri burchakli uchburchakning gipotenuzasi: c = 9.219544457292887