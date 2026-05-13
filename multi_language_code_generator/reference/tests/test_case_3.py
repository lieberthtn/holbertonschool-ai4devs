import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount3(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([{"price": 15, "category": "Electronics", "quantity": 10}])
        self.assertEqual(res["final_price"], 100.0)
if __name__ == "__main__": unittest.main()
