import os
from graphviz import Digraph
import regex as re

# def sanitize(text):
#     # clean = str(text).replace('"', "'").replace("\n", " ").strip()
#     # clean = re.sub(r"[<>\\]", "", clean)
#     # # return clean[:120] + "..." if len(clean) > 120 else clean
#     # clean = str(text)
#     # clean = clean.replace('"', "'")       # Replace double quotes with single
#     # clean = clean.replace("'", "")        # Remove single quotes entirely (optional)
#     # clean = clean.replace("\n", " ")      # Replace newlines
#     # clean = clean.replace("\r", " ")      # Replace carriage returns
#     # clean = clean.replace("\\", "")       # Remove backslashes
#     # clean = clean.replace("`", "")        # Remove backticks
#     # clean = clean.replace('"', '\\"').replace("\n", "\\n")
#     # clean = clean.replace('.', '_')
#     # clean = re.sub(r"[<>]", "", clean)    # Remove angle brackets

#     # # Collapse multiple spaces
#     # clean = re.sub(r"\s+", " ", clean).strip()
#     # Remove or replace problematic characters
#     unwanted_patterns = [r'\bn\b', r'content_', r'response_metadata', r'token_usage', r'additional_kwargs']
    
#     for pattern in unwanted_patterns:
#         text = re.sub(pattern, '', text)
#     text = re.sub(r'[^\w]', '_', text)
#     # return f'"{text}"'  # Wrap in quotes to be safe

#     # Truncate if too long
#     return text[:120] + "..." if len(text) > 120 else text

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



