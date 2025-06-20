import os
from graphviz import Digraph
import regex as re

def sanitize(text):
    # Remove unwanted terms
    unwanted_patterns = [r'\bn\b', r'content_', r'response_metadata', r'token_usage', r'additional_kwargs']
    for pattern in unwanted_patterns:
        text = re.sub(pattern, '', text)

    # Replace non-alphanumeric characters (excluding underscores) with underscores
    text = re.sub(r'[^\w]', '_', text)

    # Strip any extra spaces or underscores at the ends
    text = text.strip('_').strip()

    # Truncate the text if too long (120 characters max)
    return f'"{text[:120]}..."' if len(text) > 120 else f'"{text}"'

def export_to_svg(graph_data, file_name="output_graph"):
    dot = Digraph(format="svg")
    dot.attr(bgcolor="white")
    dot.attr("graph", rankdir="TB", ranksep="0.3", nodesep="0.2")
    dot.attr("node", shape="box", style="filled, setlinewidth(3)", width="2", fontsize="24", height="1",
             fillcolor="lightblue", color="blue", fontcolor="black")
    dot.attr("edge", arrowsize="1.4", color="gray", penwidth="2")

    seen = set()
    for node in graph_data["nodes"]:
        name = sanitize(node["name"])
        if name and name not in seen:
            dot.node(name)
            seen.add(name)

    for edge in graph_data["edges"]:
        source = sanitize(edge["source"])
        target = sanitize(edge["target"])
        if source and target:
            dot.edge(source, target)

    dot.render(f"data/outputs/{file_name}", format="svg", cleanup=True)
    return f"data/outputs/{file_name}.svg"            



