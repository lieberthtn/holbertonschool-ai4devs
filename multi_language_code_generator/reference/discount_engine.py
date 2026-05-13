import json

class DiscountEngine:
    def calculate(self, cart_items):
        subtotal = 0.0
        category_discounts = 0.0
        
        valid_items = []
        for item in cart_items:
            # Validasiya: Qiymət və kəmiyyət müsbət olmalıdır
            if item.get('price', 0) > 0 and item.get('quantity', 0) > 0:
                valid_items.append(item)
                item_total = item['price'] * item['quantity']
                subtotal += item_total
                
                # Rule 2: Electronics üçün hər məhsula $5 endirim
                if item.get('category') == 'Electronics':
                    category_discounts += (5.0 * item['quantity'])

        # Rule 3: Əvvəlcə kateqoriya endirimi tətbiq olunur
        current_total = subtotal - category_discounts
        
        # Rule 1: $100-dan çoxdursa 10% endirim
        total_discount_percent = 0.0
        if current_total > 100.0:
            total_discount_percent = current_total * 0.10
            
        total_discount = category_discounts + total_discount_percent
        final_price = subtotal - total_discount
        
        return {
            "subtotal": round(subtotal, 2),
            "category_discounts": round(category_discounts, 2),
            "total_discount": round(total_discount, 2),
            "final_price": round(max(0, final_price), 2)
        }
