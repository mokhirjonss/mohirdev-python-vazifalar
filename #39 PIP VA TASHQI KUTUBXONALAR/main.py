#39 PIP VA TASHQI KUTUBXONALAR

# Tashqi kutubxonalar bilan ishlashni o'rganamiz

# KIRISH
# Avvalgi darsimizda Python bilan birga o'rnatluvchi, standart kutubxona va undagi ba'zi foydali modullar bilan tanishdik. Ushbu darsimizda esa tashqi kutubxona bilan tanishamiz. Bu kutubxonalar yillar davomida turli foydalanuvchilar tarafidan yaratilib, yangilanib kelinadi. Bunday kutubxonalarda boshqa dasturchilar o'zlari yaratgan turli paketlarni (package) boshqalar bilan ulashadi.

# Paket (package) —modullar yig'indisi.

# Tashqi kutubxonalar va ular ichidagi paketlar shunchalik ko'pki, deyarli istalgan vazifa yoki xizmat uchun katta ehtimollik bilan kerakli dasturlar allaqachon bir nechtadan yaratilgan. Bugungi kunda Python uchun eng katta tashqi kutubxonalardan biri bu PyPi.org sahifasi.

# PIP
# Tashqi paketlarni o'rnatish uchun Pythonda maxsus pip paket menejeri mavjud. pip odatda Python bilan birga o'rnatiladi, lekin turli sabablarga ko'ra kompyuteringizda pip o'rnatilmagan bo'lsa, uni quyidagi sahifadan yuklab olishnigiz mumkin: https://pypi.org/project/pip/
# Paket menejer yordamida tashqi paketlarni o'rnatish juda oson, buning uchun Windows terminalda (cmd) (yoki  Spyder konsolida, yoki  PyCharm konsolida va hokazo)pip install paket_nomi komandasidan foydalanasiz.
# Paket nomi qanday yozilishini paketning rasmiy sahifasidan ko'rib olishingiz mumkin. Misol uchun, quyidagi rasmda googletrans paketinig sahifasi va pip komandasi qanday yozilishi ko'rsatilgan.

# Biror paketni oʻchirib tashlash uchun esa pip uninstall paket_nomi deb yozamiz.
# Ushbu darsimizning maqsadi tashqi paktelar va modullar bilan tanishish orqali, Pythonning naqadar keng qamrovli til ekanini ko'rsatish. Aslida, har bir modul haqida, ularning imkoniyatlari haqida soatlab gapirish mumkin, lekin biz vaqtni tejash maqsadida turli yo'nalishlardagi ba'zi modullar bilan tanishamiz va ularning ishlashiga sodda misollar ko'rish bilan chegaralanamiz.
# Har bir modul haqida batafsil ma'lumot olish uchun modulning sahifasiga murojat qiling.
# googletrans
# pip install googletrans
# Ushbu modul yordamida Googlening tarjimonlik xizmatiga murojat qilib, istalgan matnni turli tillarga tarjima qilishimiz mumkin. Moduldan foydalanish uchun avvalo googletrans modulidan Translator klassini import qilamiz va bu klassdan yangi obyekt yaratamiz (tarjimon). Bevosita tarjimonlik xizmatiga murojat qilish uchun tarjimon obyekti ichidagi .translate() metodiga murojat qilamiz va parametr sifatida tarjima qilish kerak bo'lgan matnni uzatamiz.

# from googletrans import Translator
# tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
# tarjima = tarjimon.translate(matn_uz)
# print(tarjima.text)
# # Python is the most popular programming language in the world
#
# # Agar boshqa tillarga tarjima qilish kerak bo'lsa, .translate() metodiga matnga qo'shimcha ravishda dest parametrini ham uzatamiz va bu parametrga tarjima qilinishi kerak bo'lgan tilning qisqartmasini beramiz. Tarjima uchun mavjuda tillarni quyidagi manzilfa ko'rishingiz mumkin: https://sites.google.com/site/opti365/translate_codes
#
# # Masalan, rus tiliga tarjima qilish ucuhn dest='ru' deb yozamiz.
#
# tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)
# # Python — самый популярный язык программирования в мире
#
# # Ingliz tilidan boshqa tillarga tarjima ham shunday:
#
# matn_en = "Tashkent is the capital of Uzbekistan"
# tarjima_uz = tarjimon.translate(matn_en, dest='uz')
# print(tarjima_uz.text)
# # Toshkent Oʻzbekistonning poytaxti
#
# # Odatda, Google asl matnning tilini o'zi aniqlaydi. Lekin matn tilini ham alohida ko'rsatmoqchi bo'lsangiz, src parametridan foydalaning:
#
# tarjima_uz = tarjimon.translate(matn_en, src='uz', dest='uz')

# requests
# pip install requests
# Bu paket yordamida Pythonda veb sahifalarga murojat qilishimiz (so'rov yuborishimiz) va ulardan qaytgan ma'lumotlar ustida turli amallar bajarishimiz mumkin. Misol uchun quyida requests yordamida kun.uz sahifasini to'liqligicha toritb olamiz:

import requests
from pprint import pprint

manzil = "https://kun.uz/news/main"
r = requests.get(manzil)
pprint(r.text)

# Ko'pincha requests paketidan APIlar bilan ishlashda foydalaniladi. API bu ma'lum bir veb hizmatga so'rov yuborish orqali undan foydalanish. Misol uchun yandex tarjimonga yoki google haritalari xizmatiga requests paketi yordamida API so'rov yuborish va o'zimizga kerakli ma'lumotlarni olishimiz mumkin. API haqida kelgusida batafsil dars qilamiz. Hozir esa sodda misola bilan cheklanamiz.
# Internetda restcountries.eu sahifasi mavjud. Bu sahifa orqali dunyodagi davlatlar haqida turli maʻlumotlarni olishingiz mumkin. Sahifadan foydalanish qulay boʻlishi uchun esa, sahifa yaratuvchilari bir nechta tayyor API lar eʻlon qilishgan. Misol uchun Oʻzbekiston haqida maʻlumot olish uchun quyidagi manzilga soʻrov yuborasiz: https://restcountries.eu/rest/v2/name/Uzbekistan
# API dan qaytgan natija JSON (lugʻat) koʻrinishda boʻladi va biz bu lugʻatdan oʻzimizga kerakli maʻlumotni sugʻurib olishimiz mumkin. Misol uchun quyidagi kodimiz APIga yuborilgan davlatning poytaxtini koʻrsatadi:

country = "Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json['capital'])

# BeautifulSoup4
# pip install beautifulsoup4
# BeautifulSoup juda kuchli modullardan biri bo'lib, bu modul yordamida turli veb sahifalardan istalgan ma'lumotlarni yig'ishtirib (scarpping) olish mumkin. Biror kishining instagram sahifasidagi barcha rasmlar deysizmi, Facebook guruhidagi barcha postlar va izohlar deysizmi, oldi-sotdi bozoridagi e'lonlar deysizmi, marhamat, bs4 moduli yordamida buni bemalol avtomatlashtirish mumkin.
# Odatda bs4 moduli requests moduli bilan hamkorlikda ishlaydi. Keling, sodda misol kor'amiz. Avvalgi bo'limda, requests yordamida kun.uz sahifasining html kodini olgan edik. Endi esa bs4 yordamida html sahifadan oxirgi yangiliklarning mavzusini ajratib olamiz.

import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)


soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")  # yangiliklarning mavzusini ajratib olamiz
print(news[0].text)  # eng birinchi yangilikni konsolga chiqaramiz

# Bu modul haqida ham kelajakda alohida dars qilamiz.

# wordcloud va matplotlib

# pip install wordcloud
# pip install matplotlib
# Wordcloud moduli yordamida katta matnlarda eng ko'p uchraydigan so'zlarni chiroyli qilib, so'zlar buluti chiqarish mumkin. 2020-yil yakunida, sariqdev sahifasida chop etilgan mashxur blogerlarning siluetlari ham aynan shu modul yordamida qilingan.

# wordcloud moduli grafiklarni chizishga mo'ljallangan matplotlib moduli bilan hamkorlikda ishlaydi.
# Quyida kun.uz sahifasidan olingan yangiliklar uchun so'zlar bulutini yaratishni ko'ramiz.

import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt


sahifa = "https://kun.uz/news/main"
news = soup.find_all(class_="news-title")
matn = ""
for n in news:
    matn += n.text

# kerakmas so'zlar
stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
# bulutni yaratamiz
wordcloud = WordCloud(width=1000, height=1000,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20).generate(matn)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

# fuzzywuzzy
# pip install fuzzywuzzy

# Bu modul yordamida so'zlarni bir-biriga solishtirish yoki matnlar tarkibida kerakli so'zni topishda foydalanamiz.
# Quyidagi misolda "salom" so'zini "assalom" va "salim" so'zlari bilan naqadar o'xshashligini tekshrib ko'ramiz:

from fuzzywuzzy import fuzz
print(fuzz.ratio("salom, assalom"))
print(fuzz.ratio("salom", "salim"))