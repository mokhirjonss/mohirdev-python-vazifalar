import unittest
from main import Car


class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""

    def test_create(self):
        # avto1 obyektini km va narhini bermasdan yaratamiz
        avto1 = Car("toyota", "camry", 2020)
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(0, avto1.get_km())
        # Yangi obyekt yaratamiz va narhini ham ko'rsatamiz
        avto2 = Car("toyota", "camry", 2020, price=75000)
        self.assertEqual(75000, avto2.price)


if __name__ == '__main__':
    unittest.main()

# Testni bajaramiz va quyidagi natijani olamiz:
# Ran 1 test in 0.001s
#
# OK
# Testimizni tahlil qilamiz. Dastaval biz obyektimiz to'g'ri yaratilayotganini tekshrish uchun avto1 obyektini 3 ta prametr bilan yaratib oldik (make, model, year) va  bu xususiyatlar bo'sh emasligini  assertIsNotNone() metodi bilan tekshirdik.
# avto1 obyektini yaratishda uning narhini ko'rsatmadik, demak bu xususiyat standart qiymat (None) ga teng bo'lishi kerak. Buni tekshirish uchun esa assertIsNone() metodiga murojat qildik. Vanihoyat, avtomobil kilometraji 0 ga teng ekanligini assertEquals() metodi yordamida test qildik.
# Test so'ngida biz yana bir obyekt yaratdik (avto2) va bu safar avtomobil narhini ko'rsatganimiz uchun assertEquals() metodi yordamida bu qiymat to'g'ri saqlanganini tekshirib oldik.
# Testlarni yozishni davom etamiz. Navbat obyektga tegishli turli metodlarga.
# Test dasturlarni alohida faylga yozishni unutmang.

