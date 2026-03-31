import pandas as pd
from graphviz import Digraph

def create_org_chart(csv_path="data/org_data.csv"):
    df = pd.read_csv(csv_path)

    dot = Digraph(format="png")
    dot.attr(rankdir="LR", splines="ortho")
    dot.attr("node", shape="box", style="rounded,filled",
             fillcolor="white", color="#3E5677")

    for _, row in df.iterrows():
        dot.node(row["parent"], row["parent"])
        dot.node(row["child"], row["child"])
        dot.edge(row["parent"], row["child"])

    dot.render("org_chart", cleanup=True)
    print("org_chart.png generated")

if __name__ == "__main__":
    create_org_chart()