import streamlit as st
import pandas as pd
from graphviz import Digraph

st.set_page_config(page_title="組織図", layout="wide")
st.title("組織図ビューア")

@st.cache_data
def load_data():
    return pd.read_csv("data/org_data.csv").fillna("")

df = load_data()

dot = Digraph()
dot.attr(rankdir="LR", splines="ortho", nodesep="0.35", ranksep="0.7")
dot.attr(
    "node",
    shape="box",
    style="rounded,filled",
    fillcolor="white",
    color="#44546A",
    fontname="Arial",
)
dot.attr("edge", color="#44546A")

nodes = set()

for _, row in df.iterrows():
    parent = str(row["parent"]).strip()
    child = str(row["child"]).strip()

    if parent and parent not in nodes:
        dot.node(parent, parent)
        nodes.add(parent)

    if child and child not in nodes:
        dot.node(child, child)
        nodes.add(child)

    if parent and child:
        dot.edge(parent, child)

st.graphviz_chart(dot, use_container_width=True)

with st.expander("元データを見る"):
    st.dataframe(df, use_container_width=True)