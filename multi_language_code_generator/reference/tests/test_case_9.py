import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount9(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([{"price": 200, "quantity": 1}])
        self.assertEqual(res["final_price"], 180.0)
if __name__ == "__main__": unittest.main()
