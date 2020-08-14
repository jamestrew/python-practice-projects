import unittest
from functions import fibonnaci, chocolate_feast

class Test_Functions(unittest.TestCase):

    def test_fibonnaci(self):
        self.assertRaises(TypeError, fibonnaci, str)
        self.assertRaises(TypeError, fibonnaci, list)
        self.assertRaises(TypeError, fibonnaci, tuple)
        self.assertRaises(TypeError, fibonnaci, dict)
        self.assertRaises(TypeError, fibonnaci, float)

        self.assertRaises(ValueError, fibonnaci, -2)

        self.assertEqual(fibonnaci(0), [])
        self.assertEqual(fibonnaci(1), [0])
        self.assertEqual(fibonnaci(2), [0, 1])
        self.assertEqual(fibonnaci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_chocolate_feast(self):
        self.assertEqual(chocolate_feast(10, 2, 5), 6)
        self.assertEqual(chocolate_feast(12, 4, 4), 3)
        self.assertEqual(chocolate_feast(6, 2, 2), 5)


if __name__ == '__main__':
    unittest.main()
