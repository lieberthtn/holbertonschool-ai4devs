# Cross-Language Specification - E-commerce Discount Engine

## Algorithm Description
The algorithm processes a list of cart items and applies various discount rules to calculate the final price.
- **Rule 1**: If the total cart value is over $100, apply a 10% discount.
- **Rule 2**: If an item belongs to the "Electronics" category, apply a flat $5 discount per item.
- **Rule 3**: Discounts are cumulative (Category discount applied first, then total cart discount).

## Input Format
A JSON array of objects representing cart items:
```json
[
  { "id": "P1", "name": "Laptop", "price": 120.00, "category": "Electronics", "quantity": 1 },
  { "id": "P2", "name": "T-Shirt", "price": 20.00, "category": "Apparel", "quantity": 2 }
]
Output Format
A JSON object with the summary:

JSON
{
  "subtotal": 160.00,
  "category_discounts": 5.00,
  "total_discount": 15.50,
  "final_price": 139.50
}
Edge Cases
Empty Cart: Should return all values as 0.00 without errors.

Zero/Negative Price: Items with price <= 0 should be ignored.

Large Cart: Should handle up to 10,000 items efficiently.

Mixed Categories: Ensure Rule 2 only affects the specific items, not the whole cart.

Test Cases
Case 1 (Standard): Cart with $120 Electronics item.

Expected: $120 -> $115 (Rule 2) -> $103.50 (Rule 1).

Case 2 (No Discounts): Cart with $30 Apparel.

Expected: final_price = 30.00.

Case 3 (Bulk Electronics): 10 Electronics items at $15 each.

Expected: subtotal $150 -> $100 (after Rule 2) -> $90 (after Rule 1).

Case 4 (Empty): Empty input array [].

Expected: final_price = 0.00.

Case 5 (Invalid Data): Cart with malformed category or negative quantity.

Expected: Invalid items skipped, valid items processed.
