from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from agents.researcher import run_researcher
from agents.summarizer import run_summarizer
from agents.mapper import run_mapper

class AgentState(TypedDict):
    input: str
    raw_info: dict
    summary: str
    result: dict

def build_graph():
    graph = StateGraph(AgentState)

    def researcher_node(state: AgentState):
        return {"raw_info": run_researcher(state["input"])}
    
    def summarizer_node(state: AgentState):
        return {"summary": run_summarizer(state["raw_info"])}
    
    def mapper_node(state: AgentState):
        return {"result": run_mapper(state["summary"])}
    
    graph.add_node("researcher", researcher_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_node("mapper", mapper_node)

    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "summarizer")
    graph.add_edge("summarizer", "mapper")
    graph.add_edge("mapper", END)

    app = graph.compile()

    return app

def autonomous_pipeline(query: str):
    app = build_graph()
    result = app.invoke({"input": query})
    return result["result"]

    
