from src.utils.scraper import WebScraperTool
from src.utils.sentiment import SentimentAnalyzerTool
from src.utils.trends import MarketTrendAnalyzerTool
from src.utils.report import ReportGeneratorTool

class SneakySalesmanAgent:
    def __init__(self):
        self.scraper = WebScraperTool()
        self.sentiment = SentimentAnalyzerTool()
        self.trends = MarketTrendAnalyzerTool()
        self.report = ReportGeneratorTool()

    def run(self, request):
        product_data = self.scraper.run(request.product, request.region)
        sentiment_data = self.sentiment.run(request.product)
        trend_data = self.trends.run(request.product, request.market)

        report = self.report.run(
            product_data=product_data,
            sentiment_data=sentiment_data,
            trend_data=trend_data
        )

        return report