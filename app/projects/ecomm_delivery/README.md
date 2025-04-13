# E-Commerce Delivery Prediction - Web Application

## Overview
This project focuses on predicting delivery times for e-commerce orders using machine learning models. The goal is to optimize delivery logistics and improve customer satisfaction by providing accurate delivery time estimates.

## Features
- **Interactive Visualizations**: Explore delivery trends and insights through interactive graphs.
- **Predictive Modeling**: Predict delivery times based on order details using machine learning models.
- **Data Insights**: Analyze key factors influencing delivery times, such as distance, order size, and traffic conditions.

## Folder Structure
```
ecomm_delivery/
├── templates/            # HTML templates for rendering the web pages
├── static/               # Static assets (CSS, JS, images)
│   ├── css/              # Stylesheets for the web application
│   ├── js/               # JavaScript files for interactive elements
│   ├── data/             # Processed datasets used for visualizations
├── utils.py              # Helper functions for data loading and graph generation
├── routes.py             # Defines the routes and logic for the web application
└── __init__.py           # Blueprint initialization
```

## Usage

### Running the App with Flask
1. Navigate to the `app` folder:
   ```git clone git@github.com:Aftabby/ecomm-delivery-project.git
   ```
2. Start the Flask application:
   ```bash
   python app.py
   ```
3. Open the app in your browser at `http://localhost:5000/ecomm-delivery`.

### Running the App with Docker
1. Build the Docker image:
   ```bash
   docker build -t ecomm-delivery-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 ecomm-delivery-app
   ```
3. Open the app in your browser at `http://localhost:5000/ecomm-delivery`.

## Technologies Used
- **Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Plotly
- **Deployment**: Docker

## Contributors
- **Aftabby** - [GitHub Profile](https://github.com/Aftabby)

## License
This project is licensed under the MIT License. See the [LICENSE](../../../../LICENSE) file for details.
