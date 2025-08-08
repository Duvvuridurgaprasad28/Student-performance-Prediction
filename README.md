# Student Performance Prediction and Analysis

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![Power BI](https://img.shields.io/badge/Power--BI-Integrated-yellow)
---
This project aims to predict students' performance in exams based on various features such as study time, past grades, and other academic-related factors. The prediction model uses machine learning algorithms to assess the data and predict student performance with high accuracy. This project combines machine learning and data visualization to predict students' academic performance and analyze performance trends using both a Streamlit web application and a Power BI dashboard.
---
## Project Overview
This application aims to predict a student’s final grade based on various academic and non-academic factors such as:
- **Study hours per week**
- **Attendance rate**
- **Previous grades**
- **Gender**
- **Parental support**
- **Participation in extracurricular activities**

The project leverages machine learning models and powerful data visualizations to provide both predictions and insights into performance influencers.
---
## Features
Machine Learning Prediction (Streamlit App):
   - **Data Preprocessing**: Cleans and processes the dataset for machine learning models.
   - **Model Building**: Builds machine learning models to predict student performance.
   - **Streamlit Web App**: A simple interactive web interface built with Streamlit to visualize and predict students' exam performance.
**Data Visualization**
   - **Power BI Dashboard**:
     - An interactive report highlighting academic performance trends and risk factors.
     - A dashboard with filters for gender and parental support, and visuals for study time vs. performance, attendance impact, and more.
---
## Power BI Dashboard
The Power BI dashboard provides an interactive report to visualize student performance, highlighting trends and risk factors. It allows for detailed analysis of various metrics, such as study hours, attendance rates, and parental support, to help identify key influencers on student grades.
The Power BI dashboard complements the Streamlit app by providing deep insights into student academic trends. It includes:
- **Gender-based filtering**
- **Parental support level impact**
- **Study hours vs. grades correlation**
- **Attendance & extracurricular activity effect
  > Power BI Dashboard Screenshot Below
  ![PowerBI](assets\powerbi.png)
--- 
Streamlit App Interface:

   > Streamlit Web App Screenshot Below
   ![streamlit](assets\streamlit.png)
---
## Tools & Libraries
- **Streamlit**: For creating an interactive web application.
- **Scikit-learn**: For building machine learning models.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **Plotly**: For interactive charts and visualizations.
- **Power BI**: Dashboard for data analysis.
---
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Duvvuridurgaprasad28/student-performance-prediction.git


2. Navigate to the project directory:

   ```bash
   cd Student-performance-prediction
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit web application:

```bash
streamlit run app.py
```

This will launch a local web server and open the app in your default browser.
---
## Usage

Once the Streamlit app is running, you can:
- Input the features such as study hours, past grades, and other factors.
- Click on the **Predict** button to see the predicted performance of the student in the exam.
- Visualize the data using interactive charts and graphs.
---
## Dataset

The dataset used in this project contains various factors that affect student performance, including:

- Name: The student's name.
- Gender: Gender of the student.
- AttendanceRate: The student's attendance percentage.
- StudyHoursPerWeek: The number of hours the student studies each week.
- PreviousGrade: The student's previous exam grade.
- ExtracurricularActivities: Participation in extracurricular activities.
- ParentalSupport: The level of parental support.
---
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---
## Acknowledgments

- Thank you to the creators of the libraries used in this project: Streamlit, scikit-learn, pandas, matplotlib, seaborn, plotly, and others.
- The dataset used in this project is publicly available.
---

### Explanation:
- **Project Title**: The title at the top describes the project.
- **Features**: A short description of what the project can do.
- **Tools & Libraries**: List the key technologies used in the project.
- **Installation**: Instructions to set up the project environment and install dependencies.
- **Running the Application**: How to run the app using Streamlit.
- **Usage**: Details about how users can interact with the Streamlit app.
- **Dataset**: Mention where the dataset is from or provide a link if you’re using an external dataset.
- **License & Acknowledgments**: Information about licensing and credit for tools and libraries used.
---
