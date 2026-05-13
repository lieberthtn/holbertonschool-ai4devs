import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount10(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([{"price": 100, "quantity": 0}])
        self.assertEqual(res["subtotal"], 0.0)
if __name__ == "__main__": unittest.main()
