import numpy as np
import pandas as pd
import json
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.utils import PlotlyJSONEncoder
from scipy.stats import gaussian_kde


def main():
    graph()
    pass


def load_sample():
    """
    Load the sample data from the specified path.
    """
    path = os.path.join(
        os.path.dirname(__file__), "static", "data", "cleaned_sleep_dataset.csv"
    )
    df = pd.read_csv(path)
    df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")
    return df


def load_compare_df():
    path = os.path.join(os.path.dirname(__file__), "static", "data", "compare_df.csv")
    df = pd.read_csv(path)
    return df


def graph():
    """
    I used plotly to visualize the data.
    I created a function to generate a graph using plotly.
    """
    df = load_sample()
    compare_df = load_compare_df()

    # % First Graph (3X3 Subplots)
    # Create a 3x3 subplot grid
    fig1 = make_subplots(
        rows=3,
        cols=3,
        subplot_titles=[
            "Gender",
            "Age",
            "Sleep Duration",
            "Quality of Sleep",
            "Physical Activity Level",
            "Stress Level",
            "BMI Category",
            "Daily Steps",
            "Sleep Disorder",
        ],
        vertical_spacing=0.2,
        horizontal_spacing=0.15,
    )

    ## Row 1
    # Gender (Countplot equivalent)
    gender_counts = df["Gender"].value_counts()
    fig1.add_trace(
        go.Bar(x=gender_counts.index, y=gender_counts.values, name="Gender"),
        row=1,
        col=1,
    )
    # Age (Histogram)
    fig1.add_trace(go.Histogram(x=df["Age"], nbinsx=10, name="Age"), row=1, col=2)
    # Sleep Duration (Histogram)
    fig1.add_trace(
        go.Histogram(x=df["Sleep Duration"], nbinsx=10, name="Sleep Duration"),
        row=1,
        col=3,
    )

    ## Row 2
    # Quality of Sleep (Countplot equivalent)
    quality_counts = df["Quality of Sleep"].value_counts()
    fig1.add_trace(
        go.Bar(
            x=quality_counts.index, y=quality_counts.values, name="Quality of Sleep"
        ),
        row=2,
        col=1,
    )
    # Physical Activity Level (Histogram)
    fig1.add_trace(
        go.Histogram(
            x=df["Physical Activity Level"], nbinsx=10, name="Physical Activity Level"
        ),
        row=2,
        col=2,
    )
    # Stress Level (Countplot equivalent)
    stress_counts = df["Stress Level"].value_counts()
    fig1.add_trace(
        go.Bar(x=stress_counts.index, y=stress_counts.values, name="Stress Level"),
        row=2,
        col=3,
    )

    ## Row 3
    # BMI Category (Countplot equivalent)
    bmi_counts = df["BMI Category"].value_counts()
    fig1.add_trace(
        go.Bar(x=bmi_counts.index, y=bmi_counts.values, name="BMI Category"),
        row=3,
        col=1,
    )
    # Daily Steps (Histogram)
    fig1.add_trace(
        go.Histogram(x=df["Daily Steps"], nbinsx=10, name="Daily Steps"), row=3, col=2
    )
    # Sleep Disorder (Countplot equivalent)
    sleep_disorder_counts = df["Sleep Disorder"].value_counts()
    fig1.add_trace(
        go.Bar(
            x=sleep_disorder_counts.index,
            y=sleep_disorder_counts.values,
            name="Sleep Disorder",
        ),
        row=3,
        col=3,
    )

    ## Update layout for better appearance
    fig1.update_layout(
        height=900,  # Base height, will scale with container
        width=1200,  # Base width, will scale with container
        title_text="Health and Sleep Data Visualizations",
        showlegend=False,
        template="plotly_white",
        margin=dict(l=60, r=60, t=100, b=60),  # Adjusted margins to prevent clipping
        font=dict(size=12),  # Base font size, will be overridden by CSS if needed
        title_font=dict(size=16),
        autosize=True,  # Allow Plotly to resize based on container
    )

    # Update subplot titles font size (relative to layout font)
    fig1.for_each_annotation(lambda a: a.update(font=dict(size=12)))

    # Update axes with responsive titles
    fig1.update_xaxes(
        title_text="Gender",
        row=1,
        col=1,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="Age", row=1, col=2, title_font=dict(size=10), tickfont=dict(size=8)
    )
    fig1.update_xaxes(
        title_text="Sleep Duration",
        row=1,
        col=3,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="Quality of Sleep",
        row=2,
        col=1,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="Physical Activity Level",
        row=2,
        col=2,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="Stress Level",
        row=2,
        col=3,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="BMI Category",
        row=3,
        col=1,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="Daily Steps",
        row=3,
        col=2,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_xaxes(
        title_text="Sleep Disorder",
        row=3,
        col=3,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )

    fig1.update_yaxes(
        title_text="Count",
        row=1,
        col=1,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=1,
        col=2,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=1,
        col=3,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=2,
        col=1,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=2,
        col=2,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=2,
        col=3,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=3,
        col=1,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=3,
        col=2,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )
    fig1.update_yaxes(
        title_text="Count",
        row=3,
        col=3,
        title_font=dict(size=10),
        tickfont=dict(size=8),
    )

    # % Second Graph
    fig2 = px.histogram(
        df,
        x="Gender",
        color="Sleep Disorder",
        barmode="group",  # to group bars side-by-side (like hue in seaborn)
        title="Gender and Sleep Disorder",
    )
    fig2.update_layout(xaxis_title="Gender", yaxis_title="Count", bargap=0.2)

    # % Third Graph
    fig3 = px.histogram(
        df,
        x="Occupation",
        color="Sleep Disorder",
        barmode="group",  # Like hue in Seaborn
        title="Occupation and Sleep Disorder",
    )

    fig3.update_layout(
        xaxis_title="Occupation",
        yaxis_title="Count",
        bargap=0.2,
        xaxis_tickangle=90,  # Rotate x-axis labels
    )

    # % Fourth Graph
    fig4 = px.histogram(
        df,
        x="BMI Category",
        color="Sleep Disorder",
        barmode="group",
        title="BMI Category and Sleep Disorder",
        color_discrete_sequence=px.colors.qualitative.Set1,  # Similar to Seaborn's 'Set1'
    )
    fig4.update_layout(xaxis_title="BMI Category", yaxis_title="Count", bargap=0.2)

    # % Fifth Graph - Model Performance
    # Extract actual and predicted values from the DataFrame
    actual = compare_df["Sleep Disorder"]
    predicted = compare_df["Decision Tree Prediction"]

    # Create KDEs
    actual_kde = gaussian_kde(actual)
    predicted_kde = gaussian_kde(predicted)

    # Define x range based on combined min/max of actual and predicted
    x_range = np.linspace(
        min(actual.min(), predicted.min()), max(actual.max(), predicted.max()), 100
    )

    # Create the Plotly figure
    fig5 = go.Figure()

    fig5.add_trace(
        go.Scatter(
            x=x_range,
            y=actual_kde(x_range),
            mode="lines",
            name="Actual Value",
            line=dict(color="red"),
        )
    )

    fig5.add_trace(
        go.Scatter(
            x=x_range,
            y=predicted_kde(x_range),
            mode="lines",
            name="Predicted Values",
            line=dict(color="blue"),
        )
    )

    # Layout settings
    fig5.update_layout(
        title="Random Forest: Actual vs Predicted Values for Sleep Disorder",
        xaxis_title="Sleep Disorder",
        yaxis_title="Proportion of People",
        template="plotly_white",
    )

    # % Sixth Graph - Model Performance
    # Extract actual and predicted values from the DataFrame
    actual = compare_df["Sleep Disorder"]
    predicted = compare_df["Random Forest Prediction"]

    # Calculate KDEs
    actual_kde = gaussian_kde(actual)
    predicted_kde = gaussian_kde(predicted)

    # Define a common x-axis range
    x_range = np.linspace(
        min(actual.min(), predicted.min()), max(actual.max(), predicted.max()), 100
    )

    # Build the Plotly figure
    fig6 = go.Figure()

    fig6.add_trace(
        go.Scatter(
            x=x_range,
            y=actual_kde(x_range),
            mode="lines",
            name="Actual Value",
            line=dict(color="red"),
        )
    )

    fig6.add_trace(
        go.Scatter(
            x=x_range,
            y=predicted_kde(x_range),
            mode="lines",
            name="Predicted Values",
            line=dict(color="blue"),
        )
    )

    fig6.update_layout(
        title="Decision Tree: Actual vs Predicted Values for Sleep Disorder",
        xaxis_title="Sleep Disorder",
        yaxis_title="Proportion of Patients",
        template="plotly_white",
    )

    # % Define graph_json to include all the grpahs as json
    graph_json = json.dumps([fig1, fig2, fig3, fig4, fig5, fig6], cls=PlotlyJSONEncoder)

    return graph_json


def load_model():
    """
    I predicted using the model and saved the data as compare_df already to save cloud resources.
    Alternatively, we can load the model and predict the data again.
    I saved the models as a pickle file in "models" folder.
    Will use this to implement API Later.
    """
    path = os.path.join(os.path.dirname(__file__), "models", "trained_models.pickle")
    pass


if __name__ == "__main__":
    main()
