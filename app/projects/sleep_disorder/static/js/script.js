const config = { responsive: true }; // Enable responsiveness

//First graph
document.addEventListener("DOMContentLoaded", () => {
  if (typeof graphData !== "undefined") {
    const modelPlotContainer = document.getElementById("graph1");
    const containerWidth = modelPlotContainer.offsetWidth;

    //First Graph
    graphData[0].layout.width = containerWidth; // Set width to container's width
    graphData[0].layout.height = 750;
    graphData[0].layout.legend = {
      orientation: "h",
      x: 0.5,
      xanchor: "center",
      y: -0.7, // Move legend further down
    };
    graphData[0].layout.margin = { l: 20, r: 20, t: 50, b: 0 }; // Reduce margins

    // Loop through the remaining graphs (2nd to 4th) and set their layout properties
    for (let i = 1; i <= 3; i++) {
      graphData[i].layout.height = 250;
      graphData[i].layout.legend = {
        orientation: "h",
        x: 0.5,
        xanchor: "center",
        y: -1, // Move legend further down
      };
      graphData[i].layout.margin = { l: 20, r: 20, t: 50, b: 30 }; // Reduce margins
    }

    for (let i = 4; i <= 5; i++) {
      graphData[i].layout.width = containerWidth; // Set width to container's width
      graphData[i].layout.height = 250;
      graphData[i].layout.legend = {
        orientation: "h",
        x: 0.5,
        xanchor: "center",
        y: -0.7, // Move legend further down
      };
      graphData[i].layout.margin = { l: 20, r: 20, t: 50, b: 0 }; // Reduce margins
    }

    graphData.forEach((graph, index) => {
      // Render the graph using Plotly with the specified data and layout
      Plotly.newPlot(`graph${index + 1}`, graph.data, graph.layout); //equivalent to graphData[index].data and graphData[index].layout and graph1, graph2 is the id of the element in HTML where graph will appear
    });
  } else {
    console.error("Graph data is not defined or is empty.");
  }
});

//Second graph
