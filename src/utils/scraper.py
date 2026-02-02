import random

class WebScraperTool:
    def run(self, product: str, region: str):
        return {
            "avg_price": random.randint(50, 150),
            "competitors": ["BrandA", "BrandB", "BrandC"],
            "platforms": ["Amazon", "Shopify"],
        }