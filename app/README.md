# Web Application Portfolio - Flask Blueprint

## Overview
This project is a portfolio of web applications built using the Flask framework. It showcases data science and machine learning skills, including data analysis, predictive modeling, and interactive visualizations. The portfolio is modularly structured using Flask blueprints for scalability and maintainability.

## Live Version
The live version of this portfolio is deployed at [www.aftabby.com](https://www.aftabby.com).

## Projects
### 1. Data Scientists Salary Prediction
- **Description**: Predicts salaries for data scientist job listings based on job attributes.
- **Features**:
  - Interactive visualizations of salary trends and job attributes.
  - Predictive modeling using machine learning algorithms.
  - Insights into key factors influencing salaries.
- **Technologies**: Flask, Plotly, Docker, HTML, CSS, JavaScript.

### 2. Sleep Disorder Prediction
- **Description**: Predicts sleep disorders such as Insomnia and Sleep Apnea using lifestyle and medical data.
- **Features**:
  - Interactive visualizations of sleep disorder insights.
  - Predictive modeling using machine learning algorithms.
  - Analysis of factors like BMI, gender, and occupation.
- **Technologies**: Flask, Plotly, Docker, HTML, CSS, JavaScript.

## Folder Structure
```
webapp-portfolio-flask-blueprint/
│
├── app/
│   ├── home/                     # Home blueprint
│   │   ├── templates/            # HTML templates for the home page
│   │   ├── static/               # Static assets (CSS, JS, images)
│   │   └── __init__.py           # Blueprint initialization
│   ├── projects/                 # Project-specific blueprints
│   │   ├── ds_salary/            # Data Scientists Salary Prediction project
│   │   │   ├── templates/        # HTML templates for the project
│   │   │   ├── static/           # Static assets (CSS, JS, data)
│   │   │   └── __init__.py       # Blueprint initialization
│   │   ├── sleep_disorder/       # Sleep Disorder Prediction project
│   │   │   ├── templates/        # HTML templates for the project
│   │   │   ├── static/           # Static assets (CSS, JS, data)
│   │   │   └── __init__.py       # Blueprint initialization
│   └── shared/                   # Shared resources across projects
│       ├── templates/            # Shared HTML templates
│       ├── static/               # Shared static assets
│       └── __init__.py           # Shared blueprint initialization
├── requirements.txt              # Python dependencies
├── app.py                        # Main Flask application file
└── README.md                     # Project documentation
```

## Usage
To run the portfolio locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/Aftabby/portfolio-flask-webapp
   cd webapp-portfolio-flask-blueprint
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Build and run the Docker container:
   ```bash
   docker build -t webapp-portfolio .
   docker run -p 5000:5000 webapp-portfolio
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open the app in your browser at `http://localhost:5000`.

## Technologies Used
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Plotly
- **Deployment**: Docker
- **Data Processing**: Pandas, NumPy
