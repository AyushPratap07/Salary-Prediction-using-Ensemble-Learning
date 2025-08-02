# 💼 Employee Salary Prediction using Ensemble Machine Learning

This project predicts employee salaries based on job title, education, experience, and location using ensemble machine learning techniques like Random Forest, Gradient Boosting, and Voting Regressor. The trained model is deployed via a Streamlit web app.

## 🔍 Problem Statement
Manual salary estimation is inefficient. This ML model automates salary prediction using historical data to support smarter compensation decisions.

## 🧠 Features Used
- `job_title`
- `education`
- `location`
- `experience`
- `salary` (target)

## ⚙️ ML Models
- Random Forest Regressor
- Gradient Boosting Regressor
- Voting Regressor (Ensemble of above two)

## 📈 Results
- Voting Regressor performed best with R² ≈ 0.92 and lowest MSE.
- Accurate predictions with generalization across diverse employee profiles.

## 🖥️ Streamlit Web App
Interactive web interface to predict salaries in real-time based on user input.

## 📦 How to Run

1. Clone this repository  
```bash
git clone https://github.com/yourusername/employee-salary-prediction.git
cd employee-salary-prediction
