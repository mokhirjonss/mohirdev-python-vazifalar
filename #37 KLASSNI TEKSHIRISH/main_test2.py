import unittest
from main import Car


class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""

    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make, model, year)
        self.avto2 = Car(make, model, year, price=self.price)

    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narhini tekshiramiz
        self.assertEqual(self.price, self.avto2.price)


if __name__ == '__main__':
    unittest.main()

# E'tibor bering, setUp() metodi ichida ba'zi o'zagruvchilar self yordamida berilgan (self.price,self.km, self.avto1, self,avto2). Bu o'zgaruvchilarga biz CarTest() klassining ichida istalgan joydan murojat qilishimiz mumkin. Shuning uchun ham, test_create() funksiyasi ichida biz yangi obyekt yaratmasdan, setUp() ichidagi avto1 va avto2 obyektlariga murojat qildik.


