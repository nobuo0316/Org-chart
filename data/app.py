import streamlit as st
import pandas as pd
from graphviz import Digraph

st.title("組織図ビューア")

df = pd.read_csv("data/org_data.csv")

dot = Digraph()
dot.attr(rankdir="LR", splines="ortho")
dot.attr("node", shape="box", style="rounded,filled",
         fillcolor="white", color="#3E5677")

for _, row in df.iterrows():
    dot.node(row["parent"], row["parent"])
    dot.node(row["child"], row["child"])
    dot.edge(row["parent"], row["child"])

st.graphviz_chart(dot)

st.subheader("データ編集（CSV）")
st.dataframe(df)
