import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3), 28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)

if __name__ == '__main__':
    unittest.main()

# Bu yerda e'tibor qiling, biz har bir funksiya uchun 2 tadan test yozdik. Testni bajaramiz va quyidagi natijani olamiz:
# Ran 2 tests in 0.001s
#
# OK

