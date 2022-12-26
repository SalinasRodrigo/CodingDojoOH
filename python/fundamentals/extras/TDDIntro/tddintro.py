import unittest
import math

def reverseList(arry):
    j=len(arry)-1
    for i in range(int(len(arry)/2)):
        arry[i], arry[j]=arry[j], arry[i]
        j-=1

    return arry

def isPalindrome(arry):
    j=len(arry)-1
    for i in range(int(len(arry)/2)):
        if (arry[i]!=arry[j]):
            return False
        j-=1
    return True

def monedas(num):
    arry=[0,0,0,0]
    if(num>25):
        aux = math.floor(num/25)
        arry[0]=aux
        num=num-(25*aux)
    if(num>10):
        aux = math.floor(num/10)
        arry[1]=aux
        num=num-(10*aux)
    if(num>5):
        aux = math.floor(num/5)
        arry[2]=aux
        num=num-(5*aux)
    if(num>0):
        arry[3]=num
    return arry

def factorialRecursivo(num):
    if (num==0):
        return 1
    return num*factorialRecursivo(num-1)

def fiboRecursivo(num):
    if (num==0):
        return 0
    if (num==1):
        return 1
    return fiboRecursivo(num-1)+fiboRecursivo(num-2)

class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
    def testTwo(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])
    def testThree(self):
        self.assertEqual(reverseList([5,4,3,2,1]), [1,2,3,4,5])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

class IsPalindromeTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(isPalindrome([1,2,3,4]), False)
    def testTwo(self):
        self.assertEqual(isPalindrome([3,2,3]), True)
    def testThree(self):
        self.assertEqual(isPalindrome([2,4,4,4,2]), True)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

class MonedasTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(monedas(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(monedas(50), [2,0,0,0])
    def testThree(self):
        self.assertEqual(monedas(32), [1,0,1,2])
    def testFour(self):
        self.assertEqual(monedas(74), [2,2,0,4])
    def testfive(self):
        self.assertEqual(monedas(21), [0,2,0,1])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

class FactorialRecursivoTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorialRecursivo(5), 120)
    def testTwo(self):
        self.assertEqual(factorialRecursivo(8), 40320)
    def testThree(self):
        self.assertEqual(factorialRecursivo(3), 6)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

class FiboRecursivoTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fiboRecursivo(5), 5)
    def testTwo(self):
        self.assertEqual(fiboRecursivo(7), 13)
    def testThree(self):
        self.assertEqual(fiboRecursivo(2), 1)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas