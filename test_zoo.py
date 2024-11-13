import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price0(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
    
    def test1(self):
        self.assertEqual(self.zoo.get_ticket_price(-2), 0)

    def test2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test2a(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test3(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test4(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test4a(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test5(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test6(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test7(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)
        
    def test8(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test9(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test9a(self):
        self.assertEqual(self.zoo.get_ticket_price(100), 100)

       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()