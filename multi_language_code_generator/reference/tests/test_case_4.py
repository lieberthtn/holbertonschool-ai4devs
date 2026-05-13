import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine
class TestDiscount4(unittest.TestCase):
    def test_logic(self):
        res = DiscountEngine().calculate([])
        self.assertEqual(res["final_price"], 0.0)
if __name__ == "__main__": unittest.main()
