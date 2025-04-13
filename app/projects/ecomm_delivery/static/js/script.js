const config = { responsive: true }; // Enable responsiveness

document.addEventListener("DOMContentLoaded", () => {
  if (typeof graphData !== "undefined") {
    const modelPlotContainer = document.getElementById("graph-container");
    const containerWidth = modelPlotContainer.offsetWidth;

    for (let i = 0; i <= 9; i++) {
      if (graphData[i]) {
        graphData[i].layout.width = 0.8 * containerWidth; // Set width to container's width
        graphData[i].layout.height = 300;
        graphData[i].layout.legend = {
          orientation: "h",
          x: 0.5,
          xanchor: "center",
          y: -0.25, // Move legend further down
        };
        graphData[i].layout.margin = { l: 20, r: 20, t: 90, b: 0 }; // Reduce margins

        // Center the graph title and make the title text smaller
        graphData[i].layout.title = {
          text: graphData[i].layout.title.text, // Preserve existing title text
          x: 0.5, // Center the title
          xanchor: "center",
          font: { size: 14 }, // Smaller font size for the title
        };
        // Make subplot titles smaller if they exist
        if (graphData[i].layout.annotations) {
          graphData[i].layout.annotations.forEach((annotation, index) => {
            if (annotation.font) {
              annotation.font.size = 10; // Smaller font size for subplot titles
            } else {
              annotation.font = { size: 10 }; // Add font property if it doesn't exist
            }

            // Adjust position to prevent overlapping vertically
            if (annotation.y) {
              annotation.y += 0.05; // Slightly move annotations upwards
            }
          });
        }
        // Make x-axis and y-axis title text smaller
        graphData[i].layout.xaxis = {
          ...graphData[i].layout.xaxis,
          title: {
            ...graphData[i].layout.xaxis?.title,
            font: { size: 12 }, // Smaller font size for x-axis title
          },
        };
        graphData[i].layout.yaxis = {
          ...graphData[i].layout.yaxis,
          title: {
            ...graphData[i].layout.yaxis?.title,
            font: { size: 12 }, // Smaller font size for y-axis title
          },
        };
      }
    }

    // Additional height for the model graph
    graphData[9].layout.height = "auto";

    graphData.forEach((graph, index) => {
      // Render the graph using Plotly with the specified data and layout
      Plotly.newPlot(`graph${index + 1}`, graph.data, graph.layout); // equivalent to graphData[index].data and graphData[index].layout and graph1, graph2 is the id of the element in HTML where graph will appear
    });
  } else {
    console.error("Graph data is not defined or is empty.");
  }
});
