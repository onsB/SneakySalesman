from src.llm import llm_generate
from src.schemas import SentimentResult, ProductReview

# creating a mock dataset of ProductReviews for sentiment analysis, based on the mock data we have of ProductInfo
mock_reviews = {
    "Macbook Pro 2024": [
        ProductReview(review_text="Amazing performance and battery life!", rating=5.0),
        ProductReview(review_text="A bit overpriced but worth it for the features.", rating=4.5),
        ProductReview(review_text="The camera quality could be better.", rating=4.0),
    ],
    "Dell XPS 13": [
        ProductReview(review_text="Great value for money.", rating=4.5),
        ProductReview(review_text="Sleek design and lightweight.", rating=4.0),
        ProductReview(review_text="Had some issues with overheating.", rating=3.5),
    ],
    "Acer Aspire 5": [
        ProductReview(review_text="Affordable and decent performance.", rating=4.0),
        ProductReview(review_text="Good for basic tasks but not gaming.", rating=3.5),
        ProductReview(review_text="Build quality feels cheap.", rating=3.0),
    ],
    "HP Spectre x360": [
        ProductReview(review_text="Versatile and powerful laptop.", rating=4.5),
        ProductReview(review_text="Battery life could be improved.", rating=4.0),
        ProductReview(review_text="Excellent display quality.", rating=5.0),
    ],
}

# analyze the customer sentiment based on the mock reviews
def analyze_sentiment(product: str) -> SentimentResult: 
    prompt = f"""
    You are a sentiment analysis expert.
    Product: {product}
    Reviews: {mock_reviews.get(product, [])}
    Analyze the overall customer sentiment based on the reviews and provide a short summary.
    """
    text = llm_generate(prompt)
    return SentimentResult(overall_sentiment=text)
