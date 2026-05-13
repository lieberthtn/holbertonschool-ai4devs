import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount5(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([{"price": -10, "quantity": 1}])
        self.assertEqual(res["subtotal"], 0.0)
if __name__ == "__main__": unittest.main()
