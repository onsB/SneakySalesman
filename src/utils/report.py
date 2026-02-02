class ReportGeneratorTool:
    def run(self, product_data, sentiment_data, trend_data):

        recommendations = []

        if sentiment_data["score"] > 0.6:
            recommendations.append("Emphasize product quality in marketing")

        if trend_data["trend"] == "growing":
            recommendations.append("Invest in this growing market")

        return {
            "product": "Analyzed Product",
            "insights": {
                "product_data": product_data,
                "sentiment": sentiment_data,
                "trend": trend_data
            },
            "recommendations": recommendations
        }
