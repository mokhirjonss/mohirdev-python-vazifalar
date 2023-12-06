# SONLARNI TEKSHIRISH
# Yuqorida matn qaytaruvchi funksiyani tekshirishni ko'rdik. Keling endi sonlar bilan ishlashni ko'ramiz. Misol tariqasida yangi circle.py modulini yaratamiz va uning ichida doiraning yuzini (  ) va perimetrini ( )  hisoblaydigan funksiyalar yozamiz:

def getArea(r, pi = 3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi * (r**2)

def getPerimeter(r, pi = 3.14159):
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2 * pi * r

# E'tibor bering, ikki funksiya ham, agar foydalanuvchi aniq qiymat bermasa,  ning qiymatini standart argument sifatida 3.14159 ga teng deb qabul qilayapti. Ushbu funksiyalarni tekshirish uchun alohida circle_test.py test dasturini yozamiz. Matnlardan farqli ravishda, sonlarni taqqoslash uchun assertAlmostEqual() metodidan foydalanamiz. Bu metod, ikki sonni nuqtadan keyin 7 xonagacha aniqlikda tekshiradi:

