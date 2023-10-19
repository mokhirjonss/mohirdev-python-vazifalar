talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")

talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'
print(talaba_0)

# BO'SH LUG'AT
# Ba'zida dastur boshida bo'sh lug'at yaratib, dastur davomida lug'atga yangi ma'lumotlar kiritib borish talab qilinishi mumkin. Bundah holatda bo'sh lug'at quyidagicha yaratiladi:

talaba_1 = {}

# Dastur davomida esa lug'atga qiymatlar kiritib borilishi mumkin:

talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# QIYMATNI O'ZGARTIRISH
# Biror kalit so'zga tegishli qiymatni o'zgartirish esa quyidgachia amalga oshiriladi:

talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH
# Lu'gatdagi biror juftlik kerak emas bo'lsa uni del operatori yordamida lug'atdan olib tashlashimiz mumkin:

talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

# LUG'ATNI QATORLARGA BO'LIB YOZISH
# Uzung lug'atlarni bir necha qatorga bo'lib yozishimiz ham mumkin. Keling quyidagi misolni ko'ramiz, siz do'stlaringizdan ular qanday telefon ishlatishini so'radingiz va javoblarni bitta lug'atga joylamoqchisiz:

telefonlar = {
 'ali': 'iphone x',
 'vali': 'galaxy s9',
 'olim': 'mi 10 pro',
 'orif': 'nokia 3310'
}

phone = telefonlar['ali']
print(f"alining telefoni {phone}")

phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')
print(phone)

# AMALIYOT
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {'ismi': 'Xuddiyev Ixtiyor', 'tugilgan yili': '24.08.1973y', 'shahri': 'Uchquduq shahar'}
onam = {'ismi': 'Xuddiyeva Mavluda', 'tugilgan yili': '25.05.1973y', 'shahri': 'Uchquduq shahar'}
singlim = {'ismi': 'Hasanova Mushtariy', 'tugilgan yili': '16.03.2006', 'shahri': 'Uchquduq shahar'}

print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan yili']}, {otam['shahri']}ida istiqomat qiladi.")
print(f"Onamning ismi {onam['ismi']}, {onam['tugilgan yili']}, {onam['shahri']}ida istiqomat qiladi.")
print(f"Singlimning ismi {singlim['ismi']}, {singlim['tugilgan yili']}, {singlim['shahri']}ida istiqomat qiladi.")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
taomlar = {'otam': 'osh', 'onam': 'shurva', 'singlim': 'manti'}
print(f"Otamning sevimli taomi {taomlar['otam']}")
print(f"Onamning sevimli taomi {taomlar['onam']}")
print(f"Singlimning sevimli taomi {taomlar['singlim']}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python = {'integer': 'целое число', 'float': 'число с плавающей запятой', 'string': 'номер строки', 'if': 'если', 'else': 'иначе'}
print(f"integer: {python['integer']}, float: {python['float']}, string: {python['string']}, if: {python['if']}, else: {python['else']}")

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
words = input('Kalit so\'z kiriting: ').lower()
print(python.get(words, 'Bunday so\'z mavjud emas'))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
if words in python:
 print(python[words])
else:
 print('Bunday so\'z mavjud emas')