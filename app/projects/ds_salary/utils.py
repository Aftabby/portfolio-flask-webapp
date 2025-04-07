import pickle
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.utils
import json
import os


def main():
    pass


def load_model():
    """
    Load the model from the specified path.
    """
    path = os.path.join(os.path.dirname(__file__), "modesl", "trained_model.pickle")
    with open(path, "rb") as file:
        models = pickle.load(file)
        model = models[
            "model"
        ]  # As we saved the model with the key "model" in a dictionary within pickle file (in model_building.py)
    return model


def load_predicted_value():
    """
    Load the prediction input data from the specified path.
    """
    path = os.path.join(
        os.path.dirname(__file__), "static", "data", "predicted_value.csv"
    )
    data = np.genfromtxt(path, delimiter=",")
    data = data.reshape(-1, 1)
    return data


def load_ground_truth():
    """
    Load the ground truth data from the specified path.
    """
    path = os.path.join(os.path.dirname(__file__), "static", "data", "ground_truth.csv")
    data = np.genfromtxt(path, delimiter=",")  # Skip the header row
    data = data.reshape(-1, 1)  # Reshape the array to have one row and multiple columns
    return data


def load_sample():
    """
    Load the sample data from the specified path.
    """
    path = os.path.join(os.path.dirname(__file__), "static", "data", "final_sample.csv")
    df = pd.read_csv(path)
    return df


def load_full_data():
    """
    Load the full data from the specified path.
    """
    path = os.path.join(os.path.dirname(__file__), "static", "data", "eda_data.csv")
    df = pd.read_csv(path)
    return df


def compare_df():
    """
    Compare the predicted values with the ground truth.
    """
    y_pred_path = os.path.join(
        os.path.dirname(__file__), "static", "data", "predicted_value.csv"
    )
    y_test_path = os.path.join(
        os.path.dirname(__file__), "static", "data", "ground_truth.csv"
    )
    y_pred = pd.read_csv(y_pred_path, header=None, names=["Predicted"])
    y_test = pd.read_csv(y_test_path, header=None, names=["Ground Truth"])

    # Create an index column
    y_pred["Index"] = y_pred.index
    y_test["Index"] = y_test.index

    # Merge both into a single DataFrame
    df = pd.merge(y_pred, y_test, on="Index")

    # Sort the DataFrame by "Index" to ensure proper ordering
    df_sorted = df.sort_values(by="Index", ascending=True)
    df_sorted.reset_index(drop=True, inplace=True)

    return df_sorted


def graph():
    df = load_full_data()
    df_plot = df.loc[:, ["python_yn", "spark", "aws", "excel"]]

    skill_count = df_plot.sum()
    df_plot = pd.DataFrame({"Skill": skill_count.index, "Count": skill_count.values})

    df_compare = compare_df()

    fig1 = px.bar(
        df_plot, x="Skill", y="Count", title="Most Demanding Skills", text="Count"
    )

    fig2 = px.histogram(
        df,
        x="avg_salary",
        nbins=5,
        title="Average Salary Distribution",
        labels={"Salary": "Average Salary (USD)"},
    )

    fig3 = go.Figure()
    fig3.add_trace(
        go.Scatter(
            x=df_compare["Index"],
            y=df_compare["Ground Truth"],
            mode="lines",  # Add markers to the line
            name="Ground Truth",
            line=dict(color="blue", width=2),  # Customize line color and width
        )
    )
    fig3.add_trace(
        go.Scatter(
            x=df_compare["Index"],
            y=df_compare["Predicted"],
            mode="lines",  # Add markers to the line
            name="Predicted",
            line=dict(color="red", width=2),  # Customize line color and width
        )
    )
    fig3.update_layout(
        title="Ground Truth vs Predictions",
        xaxis_title="Index",
        yaxis_title="Value",
        legend=dict(x=0, y=1),
        hovermode="x unified",  # Show hover details for both lines together
    )

    graph_json = json.dumps([fig1, fig2, fig3], cls=plotly.utils.PlotlyJSONEncoder)

    return graph_json


if __name__ == "__main__":
    main()
