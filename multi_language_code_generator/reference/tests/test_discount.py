import unittest
from reference.discount_engine import DiscountEngine

class TestDiscountEngine(unittest.TestCase):
    def setUp(self):
        self.engine = DiscountEngine()

    def test_case_1_standard_electronics(self):
        cart = [{"id": "P1", "price": 120.0, "category": "Electronics", "quantity": 1}]
        # 120 - 5 = 115. 115 - 11.5 = 103.5
        self.assertEqual(self.engine.calculate(cart)["final_price"], 103.5)

    def test_case_2_no_discounts(self):
        cart = [{"id": "P2", "price": 30.0, "category": "Apparel", "quantity": 1}]
        self.assertEqual(self.engine.calculate(cart)["final_price"], 30.0)

    def test_case_3_bulk_electronics(self):
        cart = [{"id": "P1", "price": 15.0, "category": "Electronics", "quantity": 10}]
        # 150 - 50 = 100. 100 - 0 (not > 100) = 100.
        self.assertEqual(self.engine.calculate(cart)["final_price"], 100.0)

    def test_case_4_empty_cart(self):
        self.assertEqual(self.engine.calculate([])["final_price"], 0.0)

    def test_case_5_invalid_price(self):
        cart = [{"id": "P1", "price": -10.0, "category": "Electronics", "quantity": 1}]
        self.assertEqual(self.engine.calculate(cart)["subtotal"], 0.0)

    def test_case_6_mixed_categories(self):
        cart = [
            {"id": "P1", "price": 50.0, "category": "Electronics", "quantity": 1},
            {"id": "P2", "price": 60.0, "category": "Apparel", "quantity": 1}
        ]
        # (50-5) + 60 = 105. 105 - 10.5 = 94.5. Subtotal=110. Discount=5+10.5=15.5.
        self.assertEqual(self.engine.calculate(cart)["final_price"], 94.5)

    def test_case_7_exactly_100(self):
        cart = [{"id": "P1", "price": 100.0, "category": "Apparel", "quantity": 1}]
        self.assertEqual(self.engine.calculate(cart)["total_discount"], 0.0)

    def test_case_8_large_quantity(self):
        cart = [{"id": "P1", "price": 1.0, "category": "Electronics", "quantity": 1000}]
        # 1000 - (5*1000) = negative, result should be 0.
        self.assertEqual(self.engine.calculate(cart)["final_price"], 0.0)

    def test_case_9_missing_category(self):
        cart = [{"id": "P1", "price": 200.0, "quantity": 1}]
        # 200 - 0 = 200. 200 - 20 = 180.
        self.assertEqual(self.engine.calculate(cart)["final_price"], 180.0)

    def test_case_10_zero_quantity(self):
        cart = [{"id": "P1", "price": 100.0, "category": "Electronics", "quantity": 0}]
        self.assertEqual(self.engine.calculate(cart)["subtotal"], 0.0)

if __name__ == '__main__':
    unittest.main()
