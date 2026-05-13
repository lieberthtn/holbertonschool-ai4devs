import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount2(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([{"price": 30, "category": "Apparel", "quantity": 1}])
        self.assertEqual(res["final_price"], 30.0)
if __name__ == "__main__": unittest.main()
