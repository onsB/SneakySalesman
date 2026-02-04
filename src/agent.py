from langgraph.graph import StateGraph, END
from typing import TypedDict

from src.schemas import ProductInfo
from src.utils.scraper import scrape_product_data
from src.utils.sentiment import analyze_sentiment
from src.utils.trends import analyze_market_trends
from src.utils.report import generate_report



class AgentState(TypedDict):
    product: str
    location: str
    product_data: ProductInfo
    sentiment: str
    trends: bool
    report: str


def scraper_node(state: AgentState):
    state["product_data"] = scrape_product_data(state["product"])
    return state


def sentiment_node(state: AgentState):
    state["sentiment"] = analyze_sentiment(state["product"])
    return state


def trends_node(state: AgentState):
    state["trends"] = analyze_market_trends(state["product"])
    return state


def report_node(state: AgentState):
    report =  generate_report(
        product=state["product"],
        location=state["location"],
        sentiment=state["sentiment"],
        trend=state["trends"],
        product_info=state["product_data"],
    )
    state["report"] = report
    return state

def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("scraper", scraper_node)
    graph.add_node("sentiment", sentiment_node)
    graph.add_node("trends", trends_node)
    graph.add_node("report", report_node)

    graph.set_entry_point("scraper")
    graph.add_edge("scraper", "sentiment")
    graph.add_edge("sentiment", "trends")
    graph.add_edge("trends", "report")
    graph.add_edge("report", END)

    return graph.compile()