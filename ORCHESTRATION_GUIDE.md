# Agent Orchestration & Testing Guide

## 🔄 Agent Orchestration Architecture

SneakySalesman uses **LangGraph** to orchestrate a linear state machine. The agent takes a single `user_request` string, extracts key inputs, gathers market signals, and returns a synthesized report.

### Pipeline Flow Diagram

```
┌───────────────┐
│  User Request │
└──────┬────────┘
       │
       ▼
┌─────────────────────┐
│  Parse Request      │ ◄── Extracts product & location
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Scraper Node       │ ◄── Gathers product data
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Sentiment Node     │ ◄── Analyzes market sentiment
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Trends Node        │ ◄── Checks market trends
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Report Node        │ ◄── Generates final report
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Final Report       │
└─────────────────────┘
```

## 🔑 Key Components

### 1. AgentState (Shared Data Structure)

```python
class AgentState(TypedDict):
    user_request: str
    product: str
    location: str
    product_data: ProductInfo
    sentiment: str
    trends: bool
    report: str
```

Each node reads from and writes to this shared state.

### 2. Orchestrated Nodes

#### Node 1: Parse Request
```python
def parse_request_node(state: AgentState):
    state["product"], state["location"] = parse_request(state["user_request"])
    return state
```
- Extracts `product` and `location` from the raw request text.

#### Node 2: Scraper
```python
def scraper_node(state: AgentState):
    state["product_data"] = scrape_product_data(state["product"])
    return state
```
- Collects factual product data.

#### Node 3: Sentiment
```python
def sentiment_node(state: AgentState):
    state["sentiment"] = analyze_sentiment(state["product"])
    return state
```
- Produces a sentiment summary.

#### Node 4: Trends
```python
def trends_node(state: AgentState):
    state["trends"] = analyze_market_trends(state["product"])
    return state
```
- Evaluates market trends.

#### Node 5: Report
```python
def report_node(state: AgentState):
    report = generate_report(
        product=state["product"],
        location=state["location"],
        sentiment=state["sentiment"],
        trend=state["trends"],
        product_info=state["product_data"],
    )
    state["report"] = report
    return state
```
- Builds the final report string.

### 3. Graph Compilation
```python
def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("parse_request", parse_request_node)
    graph.add_node("scraper", scraper_node)
    graph.add_node("sentiment", sentiment_node)
    graph.add_node("trends", trends_node)
    graph.add_node("report", report_node)

    graph.set_entry_point("parse_request")
    graph.add_edge("parse_request", "scraper")
    graph.add_edge("scraper", "sentiment")
    graph.add_edge("sentiment", "trends")
    graph.add_edge("trends", "report")
    graph.add_edge("report", END)

    return graph.compile()
```

## 🧪 Testing

Current tests validate the FastAPI endpoints and response structure.

### Run tests
```bash
pytest test/test_main.py -v
```

### What is covered
- `/health` returns `{ "status": "healthy" }`
- `/analyze` accepts a request body with `request` and returns a string report in `data`

## 📊 Example Invocation

```python
agent = build_agent()
result = agent.invoke({
    "user_request": "Analyze the market for wireless earbuds in UK."
})

print(result["report"])
```

## ✅ Summary

- The agent is a linear LangGraph pipeline.
- `parse_request` is the entry point.
- The final output is a report string returned to the API.m pytest test/agent_test.py -v --tb=short 2>&1 | head 100# Agent Orchestration Explanation & Testing Guide

## 🔄 Agent Orchestration Architecture

Your Sneaky Salesman agent is built using **LangGraph**, which creates a directed acyclic graph (DAG) that orchestrates the flow of data through multiple specialized nodes. Think of it as an assembly line where each station (node) processes the data and passes it to the next station.

### Pipeline Flow Diagram

```
┌─────────┐
│  Input  │ (product name, location)
└────┬────┘
     │
     ▼
┌─────────────────────┐
│  Scraper Node       │ ◄── Gathers product data (price, ratings, reviews)
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│  Sentiment Node     │ ◄── Analyzes customer sentiment & key themes
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│  Trends Node        │ ◄── Identifies market trends & competitors
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│  Report Node        │ ◄── Generates final market analysis
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│  Final Report       │ (summary, insights, recommendations)
└─────────────────────┘
```

## 🔑 Key Components

### 1. **AgentState (Shared Data Structure)**
```python
class AgentState(TypedDict):
    product: str              # Input: Product name
    location: str             # Input: Market location
    product_data: dict        # Output from Scraper Node
    sentiment: dict           # Output from Sentiment Node
    trends: dict              # Output from Trends Node
    report: dict              # Output from Report Node
```

The `AgentState` acts as a "message bus" where each node reads from it and writes its results back to it.

### 2. **Four Orchestrated Nodes**

#### **Node 1: Scraper Node**
```python
def scraper_node(state: AgentState):
    state["product_data"] = scrape_product_data(state["product"]).dict()
    return state
```
- **Input**: Product name from state
- **Output**: Product data (platform, price, rating, reviews)
- **Purpose**: Gather factual product information

#### **Node 2: Sentiment Node**
```python
def sentiment_node(state: AgentState):
    state["sentiment"] = analyze_sentiment(state["product"]).dict()
    return state
```
- **Input**: Product name (and optionally product_data)
- **Output**: Sentiment analysis (overall_sentiment, key_themes)
- **Purpose**: Understand customer perception

#### **Node 3: Trends Node**
```python
def trends_node(state: AgentState):
    state["trends"] = analyze_market_trends(state["product"]).dict()
    return state
```
- **Input**: Product name (and optionally other state data)
- **Output**: Market trends (price_trend, demand_trend, competitors)
- **Purpose**: Identify market dynamics

#### **Node 4: Report Node**
```python
def report_node(state: AgentState):
    combined = {
        "product_data": state["product_data"],
        "sentiment": state["sentiment"],
        "trends": state["trends"],
        "location": state["location"],
    }
    state["report"] = generate_report(state["product"], combined).dict()
    return state
```
- **Input**: All accumulated state data
- **Output**: Final market analysis report
- **Purpose**: Synthesize all data into actionable insights

### 3. **Graph Compilation**
```python
def build_agent():
    graph = StateGraph(AgentState)
    
    # Add nodes
    graph.add_node("scraper", scraper_node)
    graph.add_node("sentiment", sentiment_node)
    graph.add_node("trends", trends_node)
    graph.add_node("report", report_node)
    
    # Define execution order (edges)
    graph.set_entry_point("scraper")      # Start here
    graph.add_edge("scraper", "sentiment") # Then sentiment
    graph.add_edge("sentiment", "trends")  # Then trends
    graph.add_edge("trends", "report")     # Finally report
    graph.add_edge("report", END)          # Then end
    
    return graph.compile()
```

## 🧪 How to Test Orchestration

### Run All Agent Tests
```bash
pytest test/agent_test.py -v
```

### Test Categories

#### 1. **Orchestration Tests** - Verify complete pipeline
```bash
pytest test/agent_test.py::TestAgentOrchestration -v
```
- `test_agent_builds_successfully` - Graph compiles without errors
- `test_full_pipeline_execution` - All nodes execute end-to-end
- `test_state_flows_through_pipeline` - Data flows correctly through nodes

#### 2. **Individual Node Tests** - Test each node in isolation
```bash
pytest test/agent_test.py::TestIndividualNodes -v
```
- `test_scraper_node_output` - Scraper produces valid product data
- `test_sentiment_node_output` - Sentiment node analyzes correctly
- `test_trends_node_output` - Trends node identifies patterns
- `test_report_node_uses_accumulated_data` - Report uses all inputs

#### 3. **Node Dependency Tests** - Verify data dependencies
```bash
pytest test/agent_test.py::TestNodeDependencies -v
```
- Tests that nodes can access required data from previous nodes
- Verifies report node receives all inputs

#### 4. **Execution Order Tests** - Confirm sequential execution
```bash
pytest test/agent_test.py::TestNodeExecution -v
```
- `test_execution_order` - Nodes run in correct sequence
- `test_sequential_data_enrichment` - Each node adds data progressively

#### 5. **Error Handling Tests** - Test edge cases
```bash
pytest test/agent_test.py::TestErrorHandling -v
```
- Missing fields
- Special characters in product names
- Various locations

#### 6. **Output Validation Tests** - Verify results quality
```bash
pytest test/agent_test.py::TestAgentOutputValidation -v
```
- Report structure is correct
- Recommendations are actionable
- All analysis data is present

## 📊 Data Flow Example

Here's what happens when you invoke the agent:

```python
agent = build_agent()
result = agent.invoke({
    "product": "smartphone",
    "location": "USA"
})
```

### Step 1: Scraper Node
```
Input State:  {"product": "smartphone", "location": "USA", ...}
              ↓
Process:      Calls scrape_product_data("smartphone")
              ↓
Output State: {..., "product_data": {
                "platform": "Amazon",
                "price": 999.0,
                "rating": 4.6,
                "reviews_count": 12034
              }}
```

### Step 2: Sentiment Node
```
Input State:  {..., "product_data": {...}}
              ↓
Process:      Calls analyze_sentiment("smartphone")
              ↓
Output State: {..., "sentiment": {
                "overall_sentiment": "positive",
                "key_themes": ["battery life", "camera", "price"]
              }}
```

### Step 3: Trends Node
```
Input State:  {..., "sentiment": {...}}
              ↓
Process:      Calls analyze_market_trends("smartphone")
              ↓
Output State: {..., "trends": {
                "price_trend": "stable",
                "demand_trend": "increasing",
                "competitors": ["Samsung Galaxy", "Google Pixel"]
              }}
```

### Step 4: Report Node
```
Input State:  {..., "trends": {...}, all previous data}
              ↓
Process:      Combines all data and calls generate_report()
              ↓
Output State: {..., "report": {
                "summary": "Market analysis summary...",
                "insights": {all collected data},
                "recommendations": [...]
              }}
```

## 🎯 Key Testing Insights

### What We're Testing

1. **Orchestration** - Does LangGraph execute the nodes in the right order?
2. **Data Flow** - Does state carry data from one node to the next?
3. **Node Isolation** - Does each node work independently?
4. **Dependencies** - Are all required inputs available to each node?
5. **Output Quality** - Is the final report well-structured and complete?

### Sample Test Output

```
test/agent_test.py::TestAgentOrchestration::test_full_pipeline_execution PASSED
test/agent_test.py::TestIndividualNodes::test_scraper_node_output PASSED
test/agent_test.py::TestIndividualNodes::test_sentiment_node_output PASSED
test/agent_test.py::TestIndividualNodes::test_trends_node_output PASSED
test/agent_test.py::TestNodeExecution::test_execution_order PASSED
test/agent_test.py::TestAgentOutputValidation::test_final_report_structure PASSED
```

## 🔍 Understanding the Tests

### Example 1: Full Pipeline Test
```python
def test_full_pipeline_execution(self):
    agent = build_agent()
    result = agent.invoke({
        "product": "laptop",
        "location": "USA",
    })
    
    # Verify all state fields are populated
    assert "product_data" in result    # From scraper
    assert "sentiment" in result        # From sentiment
    assert "trends" in result           # From trends
    assert "report" in result           # From report
```
This ensures the entire orchestration completes successfully.

### Example 2: Sequential Enrichment Test
```python
def test_sequential_data_enrichment(self):
    state = {...}
    
    state = scraper_node(state)
    assert state["product_data"] != {}   # ✓ Populated
    assert state["sentiment"] == {}      # ✗ Not yet
    
    state = sentiment_node(state)
    assert state["sentiment"] != {}      # ✓ Populated
    assert state["trends"] == {}         # ✗ Not yet
    
    # ... continues for trends and report
```
This verifies each node enriches the state in the correct order.

### Example 3: Dependency Test
```python
def test_report_requires_all_previous_nodes(self):
    state = {
        "product": "phone",
        "product_data": {...},      # From scraper
        "sentiment": {...},         # From sentiment
        "trends": {...},            # From trends
    }
    
    result = report_node(state)
    insights = result["report"]["insights"]
    
    # Verify report used all inputs
    assert "product_data" in insights
    assert "sentiment" in insights
    assert "trends" in insights
```
This ensures the report node correctly incorporates all upstream data.

## 📈 Advantages of This Orchestration

1. **Modularity** - Each node is independent and testable
2. **Reusability** - Nodes can be used in different graphs
3. **Scalability** - Easy to add new nodes (e.g., price_analysis_node)
4. **Maintainability** - Changes to one node don't affect others
5. **Debugging** - Can trace data at each pipeline stage
6. **Parallelization** - Independent nodes could run in parallel

## 🚀 Running Tests with Coverage

```bash
# Run with coverage report
pytest test/agent_test.py --cov=src --cov-report=html

# Run specific test with detailed output
pytest test/agent_test.py::TestAgentOrchestration::test_full_pipeline_execution -vv

# Run and stop on first failure
pytest test/agent_test.py -x
```

## 🔗 Summary

Your agent uses LangGraph to:
1. **Define** a graph of processing nodes
2. **Pass** data through nodes via shared state
3. **Accumulate** insights at each stage
4. **Synthesize** final report from all gathered data

The tests verify this orchestration works correctly at every level!
