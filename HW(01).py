import datetime
import unittest

def my_brand(hw_assignment):
    name = "nanda eswar vimal boppudi"
    course = "Course 2024S-SSW567-A"
    pattern = "====%s===="
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")

    print(pattern % name)
    print(pattern % course)
    print(pattern % hw_assignment)
    print(pattern % now)

my_brand('Hw 01')
print('')

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if a == b or b == c or a == c:
            return "Isosceles and Right"
        else:
            return "Scalene and Right"
    elif a == b or b == c or a == c:
        return "Isosceles"   
    else:
        return "Scalene"

class TestTriangleClassification(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(classify_triangle(9, 9, 9), "Equilateral")
        self.assertEqual(classify_triangle(5, 5, 6), "Isosceles")
        self.assertEqual(classify_triangle(7, 13, 16), "Scalene")
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right")

if __name__ == "__main__":
    unittest.main()
