# Sleep Disorder Prediction - Web Application

## Overview
This project focuses on predicting sleep disorders such as Insomnia and Sleep Apnea using individual lifestyle and medical data. The goal is to enable early risk identification and intervention through machine learning models.

## Features
- **Interactive Visualizations**: Explore insights about sleep disorders through interactive graphs.
- **Predictive Modeling**: Use machine learning models to predict the likelihood of sleep disorders.
- **Data Insights**: Analyze key factors such as BMI, gender, and occupation influencing sleep disorders.

## Folder Structure
- **templates/**: Contains HTML templates for rendering the web pages.
- **static/**: Contains static assets such as CSS, JavaScript, and images.
  - **css/**: Stylesheets for the web application.
  - **js/**: JavaScript files for interactive elements and visualizations.
  - **mediaqueries.css**: Responsive design adjustments.
- **app.py**: The main Flask application file.
- **utils.py**: Helper functions for data loading and graph generation.

## Usage
To run the web application locally:
1. Navigate to the `app` folder:
   ```bash
   cd app
   ```
2. Start the Flask application:
   ```bash
   python app.py
   ```
3. Open the app in your browser at `http://localhost:5000/sleep-disorder`.

## Technologies Used
- **Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Plotly
- **Deployment**: Docker

## Contributors
- **Aftabby** - [GitHub Profile](https://github.com/Aftabby)

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
