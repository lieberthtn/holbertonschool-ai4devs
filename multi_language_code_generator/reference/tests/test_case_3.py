import unittest
import sys
import os

# Bu hissə reference qovluğunu tapmaq üçündür
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from discount_engine import DiscountEngine

class TestDiscount3(unittest.TestCase):
    def test_logic(self):
        engine = DiscountEngine()
        if 3 == 1: self.assertEqual(engine.calculate([{"price": 120, "category": "Electronics", "quantity": 1}])["final_price"], 103.5)
        elif 3 == 2: self.assertEqual(engine.calculate([{"price": 30, "category": "Apparel", "quantity": 1}])["final_price"], 30.0)
        elif 3 == 3: self.assertEqual(engine.calculate([{"price": 15, "category": "Electronics", "quantity": 10}])["final_price"], 100.0)
        elif 3 == 4: self.assertEqual(engine.calculate([])["final_price"], 0.0)
        elif 3 == 5: self.assertEqual(engine.calculate([{"price": -10, "quantity": 1}])["subtotal"], 0.0)
        elif 3 == 6: self.assertEqual(engine.calculate([{"price": 50, "category": "Electronics", "quantity": 1}, {"price": 60, "category": "Apparel", "quantity": 1}])["final_price"], 94.5)
        elif 3 == 7: self.assertEqual(engine.calculate([{"price": 100, "quantity": 1}])["total_discount"], 0.0)
        elif 3 == 8: self.assertEqual(engine.calculate([{"price": 1, "category": "Electronics", "quantity": 1000}])["final_price"], 0.0)
        elif 3 == 9: self.assertEqual(engine.calculate([{"price": 200, "quantity": 1}])["final_price"], 180.0)
        else: self.assertEqual(engine.calculate([{"price": 100, "quantity": 0}])["subtotal"], 0.0)

if __name__ == "__main__":
    unittest.main()
