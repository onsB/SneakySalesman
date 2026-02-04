from typing import List
from src.schemas import ProductInfo

# Create a mock object containing multiple product data rows
products: List[ProductInfo] = [
    ProductInfo(
        product="Macbook Pro 2024",
        price=2499.99,
        rating=4.8,
        tier="premium",
        category="laptop",
        seasonal=False
    ),
    ProductInfo(
        product="Dell XPS 13",
        price=1199.99,
        rating=4.5,
        tier="midrange",
        category="laptop",
        seasonal=False
    ),
    ProductInfo(
        product="Acer Aspire 5",
        price=549.99,
        rating=4.0,
        tier="budget",
        category="laptop",
        seasonal=True
    ),
    ProductInfo(
        product="HP Spectre x360",
        price=1399.99,
        rating=4.6,
        tier="midrange",
        category="laptop",
        seasonal=False
    )
]
def scrape_product_data(product: str) -> ProductInfo:
    # In a real implementation, this function would scrape data from e-commerce sites
    # Here, we return mock data based on the product name
    for p in products:
        if p["product"].lower() == product.lower():
            return p
    # Default mock data if product not found
    return ProductInfo(
        product=product,
        price=999.99,
        rating=4.2,
        tier="midrange",
        category="electronics",
        seasonal=False
    )