# API Requirements – Inventory Management API

## Domain
E-commerce inventory and product management.

## Target Users
- **Store Managers**: To track and update product availability.
- **Developers**: To integrate inventory data with the frontend storefront.
- **Analysts**: To monitor stock levels and pricing trends.

## Core Operations
1.  **Create Product**: Add a new item to the inventory.
2.  **Get All Products**: List all products with pagination.
3.  **Get Product by ID**: Retrieve detailed info for a specific SKU.
4.  **Update Product Details**: Edit name, description, or category.
5.  **Update Stock Level**: Specifically adjust the quantity of an item.
6.  **Delete Product**: Remove an item from the system.
7.  **Search Products**: Filter products by name or category.
8.  **Low Stock Alert**: Get a list of products where quantity is below a threshold.
9.  **Apply Discount**: Bulk update prices for a specific category.
10. **Batch Import**: Create multiple products at once via JSON array.
11. **Get Categories**: List all unique product categories.
12. **Audit Logs**: View history of stock changes for a product.

## Data Rules
- **SKU (Stock Keeping Unit)**: Must be unique and follow the format `PROD-XXXX`.
- **Price**: Must be a positive decimal value greater than 0.
- **Stock Quantity**: Cannot be negative; must be an integer.
- **Product Name**: Minimum 3 characters, maximum 100 characters.
- **Category**: Must belong to a predefined list of valid categories.

## Non-Functional Requirements
- **Latency**: API responses must be returned in less than 200ms.
- **Authentication**: All write operations require JWT (JSON Web Token) authentication.
- **Rate Limiting**: Maximum 100 requests per minute per API key.
- **Format**: All data exchange must be in JSON format.
