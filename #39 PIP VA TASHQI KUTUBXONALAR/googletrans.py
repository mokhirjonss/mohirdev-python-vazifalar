from googletrans import Translator
tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)
# Python is the most popular programming language in the world

# Agar boshqa tillarga tarjima qilish kerak bo'lsa, .translate() metodiga matnga qo'shimcha ravishda dest parametrini ham uzatamiz va bu parametrga tarjima qilinishi kerak bo'lgan tilning qisqartmasini beramiz. Tarjima uchun mavjuda tillarni quyidagi manzilfa ko'rishingiz mumkin: https://sites.google.com/site/opti365/translate_codes

# Masalan, rus tiliga tarjima qilish ucuhn dest='ru' deb yozamiz.

tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru.text)
# Python — самый популярный язык программирования в мире

# Ingliz tilidan boshqa tillarga tarjima ham shunday:

matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)
# Toshkent Oʻzbekistonning poytaxti

# Odatda, Google asl matnning tilini o'zi aniqlaydi. Lekin matn tilini ham alohida ko'rsatmoqchi bo'lsangiz, src parametridan foydalaning:

tarjima_uz = tarjimon.translate(matn_en, src='uz', dest='uz')
