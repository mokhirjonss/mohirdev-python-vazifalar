#38 PYTHON STANDART KUTUBXONASI
# Pythondagi foydali modullar bilan tanishamiz.

# KIRISH
# Python dasturlash tili yildan-yilga ommalashib bormoqda. Bunga birinchi navbatda Pythonning sodda va tushunarli sintaksi sabab bo'lsa, ikkinchi va ehtimol eng ko'zga ko'ringan sabab bu Pythonning keng qamrovli kutubxonalar to'plamidir. Ushbu darsimizda Pytyon kutubxonasidagi ba'zi muhim modullar bilan tanishamiz. Standart kutubxonanig to'liq tarkibi bilan Python rasmiy sahifasida tanishishingiz mumkin.
# Kutubxona bu boshqalar tarafidan yozilgan tayyor funksiyalar va obyektlar to'plami.

# datetime — SANA VA VAQT
# Ushbu modul yordamida Pythonda sanalar bilan ishlashimiz mumkin. Moduldan foydalanishdan avval uni import qilamiz. Har gal moduldan foydalanishda datetime deb qayta yozmaslik uchun, import qilishda modulga dt nomini beramiz.

import datetime as dt

# Hozirgi vaqt va sanani koʻrish uchun datetime.now() moduliga murojat qilamiz:

hozir = dt.datetime.now()
print(hozir)
# 2023-12-06 20:43:01.171301

# Kurib turganingizdek, natija yil, oy, kun soat, minut, sekund va millisekund koʻrinishida chiqdi. Biz bu qiymatlardan istaganimzni maxsus metodlar yordamida ajratib olishimiz mumkin:

# sanani ajratib olish
print(hozir.date())
# 2023-12-06

# vaqtni ajratib olish
print(hozir.time())
# 20:49:23.591814

# soatni ajratib olish
print(hozir.hour)
# 20

# minutni ajratib olish
print(hozir.minute)
# 50

# sekundni ajratib olish
print(hozir.second)
# 38

# Agar bugungi kunning sanasi talab qilinsa datetime moduli ichidagi date.today() moduliga murojat qilamiz.
bugun = dt.date.today()
print(f"Bugungu sana: {bugun}")
# Bugungu sana: 2023-12-06

# Agar biror sanani qoʻlda kiritish talab qilinsa .date() metodiga kerakli sanani (yil, oy, kun) koʻrinishida kiritamiz.

ertaga = dt.date(2023, 12, 7)
print(f"Ertangi sana: {ertaga}")
# Ertangi sana: 2023-12-07

# Faqatgina vaqt bilan ishlash uchun .datetime.now().time() metodiga murojat qilishimiz mumkin:
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
# Hozir soat: 21:02:16.992038

# Istalgan vaqtni qoʻlda kiritish uchun esa .time() metodiga kerakli vaqtni (soat, minut, sekund) koʻrinishida beramiz:
vaqtKeyin = dt.time(23, 45, 00)
print(vaqtKeyin)
# 23:45:00

# Ayirish operatori yordamida sanalalar va vaqtlar orasidagi farqni hisoblashimiz mumkin:
bugun = dt.date.today()
ramazon = dt.date(2024, 4, 13)
farq = ramazon - bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi.")
# Ramazonga 129 kun qoldi.

# Huddi shu kabi ikki vaqt oraligʻini sekundlarda yoki soatlarda ham koʻrishimiz mumkin:

hozir = dt.datetime.now()
futbol = dt.datetime(2023, 12, 6, 21, 20, 00)
farq = futbol - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar / 60)
soatlar = int(minutlar / 60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")
# Futbol boshlanishiga 86170 sekund qoldi
# Futbol boshlanishiga 1436 minut qoldi
# Futbol boshlanishiga 23 soat qoldi

# Yuqorida sanalar AQSh standartiga koʻra, yil-oy-kun koʻrinishida chiqayapti. Sanani oʻzimizga moslab chiqarish uchun .strftime() metodini chaqiramiz, va sanani oʻzimizga qulay formatda chiqaramiz.
# vatni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")

# sanani kun-oy-yil ko'rinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

# sanani kun/oy/yil ko'rinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)
# Hozir soat: 21:29:00
# Bugun sana: 06-12-2023
# 06/12/2023, 21:29

# math —MATEMATIK FUNKSIYALAR
# Bu modul oʻz ichida matematikaga oid turli funksilayar va oʻzgaruvchilarni saqlaydi. Keling, ularning baʻzilari bilan tanishamiz.

# pi ning qiymati
import math
PI = math.pi
print(f"PI ning qiymati: {PI}")
# PI ning qiymati: 3.141592653589793

# e — natural logarifm asosi
E = math.e
print(f"e ning qiymati: {E}")
# e ning qiymati: 2.718281828459045

# Trigonometriya
# Modul tarkibida deyarli barcha trigonometrik funksiyalar mavjud (cos, sin, tangens, arccos, va hokazo)

math.sin(math.pi/2)
math.cos(0)
math.tan(PI)

# Shunigdek degrees va radians metodlari yordamida burchakdan radianga va aksincha konvertasiya qilishimiz ham mumkin:
math.degrees(math.pi/2)
math.radians(90)

# LOGARIFMLAR
# log() va log10() funksiyalari yordamida natural va o'n asosli logarifmlarni hisoblash mumkin:

# natural logarifm
math.log(5)
# 10 asosli lagarifm
math.log10(100)

# SONLARNI YAXLITLASH
# Sonlarni eng yaxlitlash uchun Pythonda maxsus round() funksiyasi mavjud. Bunga qo'shimcha ravishda, math moduli ichidagi ceil() funksiyasi yordamida berilgan o'nlik sonni keyingi butun songa, floor() yordamida esa quyi butun songa yaqinlashtirish mumkin:
x = 4.6
print(math.ceil(x))
print(math.floor(x))
# 5
# 4

# ILDIZ VA DARAJA
# Berilgan sonning kvadrat ildizini hisoblash uchun sqrt(), sonni darajaga oshirish uchun esa pow() funksiyalariga murojat qilamiz:

x = 81

# kvadrat ildiz
math.sqrt(x)

# darajaga oshirish
math.pow(x, 3)  # x ning kubi
math.pow(x, 5)  # x ning 5-darajasi
math.pow(x, 1 / 3)  # x dan kub ildiz

# math moduli tarkibida boshqa funksiyalar ham mavjud. Yuqorida biz ularning ba'zilari bilan tanishdik. Bu modul asosan butun va oʻnlik sonlar bilan ishlashga moʻljallangan. Kompleks sonlar bilan ishlash uchun cmath moduliga murojat qilishingiz mumkin.

# pprint - CHIROYLI PRINT
# pprint moduli yordamida turli o'zgaruvchilarni chiroyli ko'rinishda konsolga chiqarishimiz mumkin. Bu bizga uzun lug'atlar, JSON fayllar yoki matnlar bilan ishlashda juda asqotadi.
# Misol uchun, avvalgi darslarimizning birida yaratgan bemor.json faylini ochamiz va avval print() keyin pprint() yordamida konsolga chiqaramiz.

from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(bemor)
# {'ism': 'Alijon Valiyev', 'yosh': 30, 'oila': True, 'farzandlar': ['Ahmad', 'Bonu'], 'allergiya': None, 'dorilar': [{'nomi': 'Analgin', 'miqdori': 0.5}, {'nomi': 'Panadol', 'miqdori': 1.2}]}
pprint(bemor)
# {'allergiya': None,
#  'dorilar': [{'miqdori': 0.5, 'nomi': 'Analgin'},
#              {'miqdori': 1.2, 'nomi': 'Panadol'}],
#  'farzandlar': ['Ahmad', 'Bonu'],
#  'ism': 'Alijon Valiyev',
#  'oila': True,
#  'yosh': 30}






