# MANTIQIY QIYMATLARNI TEKSHIRISH
# Agar funksiya mantiqiy qiymat qaytarsa, bunday funksiyalarni assertTrue() va assertFalse() metodlari yordamida tekshirishimiz mumkin.
# Quyidagi funksiyamiz kiritilgan son tub yoki yo'q ekanini tekshiradi:

def tubSonmi(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2): # faqat toq sonlarni tekshiramiz
        if n % i == 0:
            return False
    return True

# Funksiyani alohida tubSonmi.py fayliga saqlaymiz. Funksiyani tekshirish uchun tubSon_test.py dasturini yozamiz: