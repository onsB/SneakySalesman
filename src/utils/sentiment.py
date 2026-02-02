class SentimentAnalyzerTool:
    def run(self, product: str):
        return {
            "score": 0.7,
            "positive_topics": ["quality", "battery"],
            "negative_topics": ["price"]
        }
