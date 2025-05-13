import streamlit as st
from workflows.langgraph_router import autonomous_pipeline
from utils.graphviz_exporter import export_to_svg
import base64

st.set_page_config(page_title="Career Roadmap Builder", page_icon=":robot_face:", layout="wide")
st.title("Career Roadmap Builder")

st.markdown("""
<style>
            .title {
                font-size: 36px;
                font-weight: weight;
                color: white;
                text-align: center;
            }
            .desc {
                text-align: center;
                font-size: 16px;
                color: white;
                margin-bottom: 30px;
            }
            .footer {
                text-align: center;
                font-size: 13px;
                color: white;
                margin-top: 40px;
            }
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='title'>Multi-Agent Career Roadmap Builder</div>
    <div class='desc'>Get detailed, AI-generated mind maps and learning roadmaps.</div>
""", unsafe_allow_html=True)

topic = st.text_input("Enter a question or topic (e.g., 'Roadmap for Machine Learning')")

if topic:
    with st.spinner("Roadmap Generating..."):
        graph = autonomous_pipeline(topic)
        svg_path = export_to_svg(graph)
        st.success("Roadmap Generated Successfully!")
        st.image(svg_path, caption=f"Visual Roadmap for: {topic}", use_column_width=True)

        with open(svg_path, "rb") as f:
            svg_data = f.read()
            b64 = base64.b64encode(svg_data).decode()
            href = f'<a href="data:image/svg+xml;base64,{b64}" download="roadmap.svg">Download Roadmap</a>'
            st.markdown(href, unsafe_allow_html=True)