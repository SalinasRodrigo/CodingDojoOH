import unittest
class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result+=num
        for i in nums:
            self.result+=i
        return self

    def subtract(self, num, *nums):
        self.result-=num
        for i in nums:
            self.result-=i
        return self

class AddTest(unittest.TestCase):
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.add(2).add(2,5,1).result, 10)
    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2,5,1,8,7,1).result, 24)
    def testThree(self):
        md = MathDojo()
        self.assertEqual(md.add(2).add(5,1).add(1,1,1,1,1).result, 13)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

class SubtractTest(unittest.TestCase):
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.subtract(2).subtract(2,5,1).result, -10)
    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.subtract(2,5,1,8,7,1).result, -24)
    def testThree(self):
        md = MathDojo()
        self.assertEqual(md.subtract(2).subtract(5,1).subtract(1,1,1,1,1).result, -13)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

class AddSubtractTest(unittest.TestCase):
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.add(2).add(2,5,1).subtract(3,2).result, 5)
    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2,5,1,8,7,1).subtract(3,2,5,4).result, 10)
    def testThree(self):
        md = MathDojo()
        self.assertEqual(md.add(2).subtract(3,2,5,4).result, -12)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas