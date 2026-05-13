import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount6(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([{"price": 50, "category": "Electronics", "quantity": 1}, {"price": 60, "category": "Apparel", "quantity": 1}])
        self.assertEqual(res["final_price"], 94.5)
if __name__ == "__main__": unittest.main()
