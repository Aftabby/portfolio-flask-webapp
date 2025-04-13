import pandas as pd
import json
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.utils import PlotlyJSONEncoder
from sklearn.metrics import accuracy_score


def main():
    graph()
    pass


def load_sample():
    path = os.path.join(
        os.path.dirname(__file__), "static", "data", "cleaned_E_Commerce.csv"
    )
    df = pd.read_csv(path)
    return df


def load_compare_df():
    path = os.path.join(os.path.dirname(__file__), "static", "data", "compare_df.csv")
    df = pd.read_csv(path)
    return df


def graph():
    df = load_sample()
    compare_df = load_compare_df()

    # % First Graph
    gender_counts = df["Gender"].value_counts().reset_index()
    gender_counts.columns = ["Gender", "Count"]
    # Create pie chart
    fig1 = px.pie(
        gender_counts,
        names="Gender",
        values="Count",
        title="Gender Distribution",
        hole=0,  # Set to 0.4 for donut-style
    )
    fig1.update_traces(textinfo="percent+label", rotation=90)

    # % Second Graph
    # Create subplots: 1 row, 3 columns
    fig2 = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=(
            "Weight Distribution",
            "Product Importance",
            "Cost of the Product",
        ),
    )
    # Plot 1: Histogram + KDE for Weight_in_gms
    fig2.add_trace(
        go.Histogram(
            x=df["Weight_in_gms"],
            name="Weight",
            histnorm="probability density",
            marker_color="skyblue",
            opacity=0.6,
        ),
        row=1,
        col=1,
    )
    # Plot 2: Count plot for Product_importance
    importance_counts = df["Product_importance"].value_counts().sort_index()
    fig2.add_trace(
        go.Bar(
            x=importance_counts.index,
            y=importance_counts.values,
            name="Product Importance",
            marker_color="orange",
        ),
        row=1,
        col=2,
    )
    # Plot 3: Histogram + KDE for Cost_of_the_Product
    fig2.add_trace(
        go.Histogram(
            x=df["Cost_of_the_Product"],
            name="Cost",
            histnorm="probability density",
            marker_color="mediumseagreen",
            opacity=0.6,
        ),
        row=1,
        col=3,
    )
    # Layout config
    fig2.update_layout(
        title_text="Product Feature Distributions",
        showlegend=False,
        height=500,
        width=1000,
        template="plotly_white",
    )

    # % Third Graph
    # Create 1 row, 3 column subplots
    fig3 = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=("Warehouse Block", "Mode of Shipment", "Reached on Time"),
    )
    # Plot 1: Warehouse Block
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    fig3.add_trace(
        go.Bar(
            x=warehouse_counts.index,
            y=warehouse_counts.values,
            name="Warehouse Block",
            marker_color="lightblue",
        ),
        row=1,
        col=1,
    )
    # Plot 2: Mode of Shipment
    shipment_counts = df["Mode_of_Shipment"].value_counts().sort_index()
    fig3.add_trace(
        go.Bar(
            x=shipment_counts.index,
            y=shipment_counts.values,
            name="Mode of Shipment",
            marker_color="lightgreen",
        ),
        row=1,
        col=2,
    )
    # Plot 3: Reached on Time
    time_counts = df["Reached.on.Time_Y.N"].value_counts().sort_index()
    fig3.add_trace(
        go.Bar(
            x=time_counts.index.astype(str),
            y=time_counts.values,
            name="Reached on Time",
            marker_color="salmon",
        ),
        row=1,
        col=3,
    )
    # Update layout
    fig3.update_layout(
        title_text="Delivery Metrics Overview",
        showlegend=False,
        height=500,
        width=1000,
        template="plotly_white",
    )

    # % Fourth graph
    # Create a 2x2 grid of subplots
    fig4 = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Customer Care Calls",
            "Customer Rating",
            "Prior Purchases",
            "Discount Offered",
        ),
    )
    # Plot 1: Customer Care Calls
    care_calls_counts = df["Customer_care_calls"].value_counts().sort_index()
    fig4.add_trace(
        go.Bar(
            x=care_calls_counts.index.astype(str),
            y=care_calls_counts.values,
            marker_color="cornflowerblue",
            name="Customer Care Calls",
        ),
        row=1,
        col=1,
    )
    # Plot 2: Customer Rating
    rating_counts = df["Customer_rating"].value_counts().sort_index()
    fig4.add_trace(
        go.Bar(
            x=rating_counts.index.astype(str),
            y=rating_counts.values,
            marker_color="mediumseagreen",
            name="Customer Rating",
        ),
        row=1,
        col=2,
    )
    # Plot 3: Prior Purchases
    purchases_counts = df["Prior_purchases"].value_counts().sort_index()
    fig4.add_trace(
        go.Bar(
            x=purchases_counts.index.astype(str),
            y=purchases_counts.values,
            marker_color="orange",
            name="Prior Purchases",
        ),
        row=2,
        col=1,
    )
    # Plot 4: Discount Offered (Histogram)
    fig4.add_trace(
        go.Histogram(
            x=df["Discount_offered"],
            histnorm="probability density",
            name="Discount Offered",
            marker_color="indianred",
            opacity=0.7,
        ),
        row=2,
        col=2,
    )
    # Layout styling
    fig4.update_layout(
        title_text="Customer Behavior Analysis",
        showlegend=False,
        height=700,
        width=1000,
        template="plotly_white",
    )

    # % Fifth graph
    # Ensure 'Reached.on.Time_Y.N' is string for labeling clarity
    df["Reached.on.Time_Y.N"] = df["Reached.on.Time_Y.N"].astype(str)
    # Create grouped bar chart
    fig5 = px.histogram(
        df,
        x="Gender",
        color="Reached.on.Time_Y.N",
        barmode="group",
        title="Gender vs Reached on Time",
        color_discrete_sequence=px.colors.qualitative.Set2,
        labels={"Reached.on.Time_Y.N": "Reached On Time"},
    )
    fig5.update_layout(template="plotly_white")

    # % Sixth graph
    # Create subplots
    fig6 = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=(
            "Weight Distribution",
            "Product Importance",
            "Cost of the Product",
        ),
    )
    # Plot 1: Violin plot for Weight_in_gms
    for val in df["Reached.on.Time_Y.N"].unique():
        fig6.add_trace(
            go.Violin(
                y=df[df["Reached.on.Time_Y.N"] == val]["Weight_in_gms"],
                x=[val] * len(df[df["Reached.on.Time_Y.N"] == val]),
                name=f"Reached: {val}",
                box_visible=True,
                meanline_visible=True,
            ),
            row=1,
            col=1,
        )
    # Plot 2: Count plot for Product_importance by Reached.on.Time_Y.N
    product_counts = (
        df.groupby(["Product_importance", "Reached.on.Time_Y.N"])
        .size()
        .reset_index(name="count")
    )
    fig6_2 = px.bar(
        product_counts,
        x="Product_importance",
        y="count",
        color="Reached.on.Time_Y.N",
        barmode="group",
    )
    for trace in fig6_2.data:
        fig6.add_trace(trace, row=1, col=2)
    # Plot 3: Violin plot for Cost_of_the_Product
    for val in df["Reached.on.Time_Y.N"].unique():
        fig6.add_trace(
            go.Violin(
                y=df[df["Reached.on.Time_Y.N"] == val]["Cost_of_the_Product"],
                x=[val] * len(df[df["Reached.on.Time_Y.N"] == val]),
                name=f"Reached: {val}",
                box_visible=True,
                meanline_visible=True,
                showlegend=False,  # Hide duplicate legend
            ),
            row=1,
            col=3,
        )
    # Layout settings
    fig6.update_layout(
        title="Delivery Analysis Based on Time Reached",
        showlegend=True,
        height=500,
        width=1200,
        template="plotly_white",
    )

    # % Seventh graph
    # Grouped counts for Warehouse_block and Mode_of_Shipment
    warehouse_counts = (
        df.groupby(["Warehouse_block", "Reached.on.Time_Y.N"])
        .size()
        .reset_index(name="count")
    )
    shipment_counts = (
        df.groupby(["Mode_of_Shipment", "Reached.on.Time_Y.N"])
        .size()
        .reset_index(name="count")
    )
    # Create subplots
    fig7 = make_subplots(
        rows=1, cols=2, subplot_titles=["Warehouse Block", "Mode of Shipment"]
    )
    # Warehouse Block plot
    warehouse_plot = px.bar(
        warehouse_counts,
        x="Warehouse_block",
        y="count",
        color="Reached.on.Time_Y.N",
        barmode="group",
    )
    for trace in warehouse_plot.data:
        fig7.add_trace(trace, row=1, col=1)
    # Mode of Shipment plot
    shipment_plot = px.bar(
        shipment_counts,
        x="Mode_of_Shipment",
        y="count",
        color="Reached.on.Time_Y.N",
        barmode="group",
    )
    for trace in shipment_plot.data:
        fig7.add_trace(trace, row=1, col=2)
    # Layout adjustments
    fig7.update_layout(
        title_text="Delivery Analysis by Warehouse and Shipment Mode",
        showlegend=True,
        width=1000,
        height=500,
        template="plotly_white",
    )

    # % Eighth graph
    # Subplot structure
    fig8 = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=[
            "Customer Care Calls",
            "Customer Rating",
            "Prior Purchases",
            "Discount Offered",
        ],
    )

    # Countplot equivalents
    def add_countplot_to_fig(col, row, x_var):
        count_df = (
            df.groupby([x_var, "Reached.on.Time_Y.N"]).size().reset_index(name="count")
        )
        bar_fig = px.bar(
            count_df, x=x_var, y="count", color="Reached.on.Time_Y.N", barmode="group"
        )
        for trace in bar_fig.data:
            fig8.add_trace(trace, row=row, col=col)

    # Add first 3 bar plots
    add_countplot_to_fig(1, 1, "Customer_care_calls")
    add_countplot_to_fig(2, 1, "Customer_rating")
    add_countplot_to_fig(1, 2, "Prior_purchases")
    # Violin plot
    violin_fig = px.violin(
        df,
        x="Reached.on.Time_Y.N",
        y="Discount_offered",
        box=True,
        points="all",
        color="Reached.on.Time_Y.N",
    )
    for trace in violin_fig.data:
        fig8.add_trace(trace, row=2, col=2)
    # Update layout
    fig8.update_layout(
        height=800,
        width=1000,
        title_text="Customer Behavior and Delivery Timeliness",
        showlegend=True,
        template="plotly_white",
    )

    # % Ninth graph
    fig9 = px.violin(
        df,
        x="Customer_care_calls",
        y="Cost_of_the_Product",
        box=True,  # Adds box plot inside violin
        points="all",  # Shows all individual points
        color="Customer_care_calls",  # Optional: adds color distinction
    )
    fig9.update_layout(
        title="Cost of the Product by Customer Care Calls",
        template="plotly_white",
        showlegend=False,
    )

    # % Tenth graph - Model Performance Comparison
    # Define model names
    models = [
        "Random Forest Classifier",
        "Decision Tree Classifier",
        "Logistic Regression",
        "KNN Classifier",
    ]
    # Compute accuracy using compare_df
    accuracy = [
        accuracy_score(compare_df["actual"], compare_df["rfc_pred"]),
        accuracy_score(compare_df["actual"], compare_df["dtc_pred"]),
        accuracy_score(compare_df["actual"], compare_df["lr_pred"]),
        accuracy_score(compare_df["actual"], compare_df["knn_pred"]),
    ]
    # Create a dataframe for plotting
    acc_df = pd.DataFrame({"Model": models, "Accuracy": accuracy})
    # Plot using plotly
    fig10 = px.bar(
        acc_df,
        x="Model",
        y="Accuracy",
        text="Accuracy",
        title="Model Comparison",
        color="Model",
        color_discrete_sequence=px.colors.sequential.Magma,
    )
    fig10.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig10.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        xaxis_tickangle=45,
        xaxis=dict(showticklabels=False),  # Disable x-axis tick labels
        template="plotly_white",
    )

    # % Define graph_json to include all the grpahs as json
    graph_json = json.dumps(
        [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10],
        cls=PlotlyJSONEncoder,
    )

    return graph_json


if __name__ == "__main__":
    main()
