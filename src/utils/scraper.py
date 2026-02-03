from src.schemas import ProductData


def scrape_product_data(product: str) -> ProductData:
    # Mocked data
    return ProductData(
        platform="Amazon",
        price=999.0,
        rating=4.6,
        reviews_count=12034,
    )