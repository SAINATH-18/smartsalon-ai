SmartSalon AI – Salon Service Recommendation System

Project Overview

SmartSalon AI is a Machine Learning based web application that recommends suitable salon services based on customer attributes such as age, gender, skin type, hair type, occasion, and budget.
The system helps salon chains standardize service recommendations, reduce staff dependency, and improve customer experience.

---

Problem Statement

Salon chains often face inconsistent service recommendations across different branches because recommendations depend on staff experience. Customer data is not properly used for decision making, and personalized service suggestions are not available.

---

Solution

SmartSalon AI uses Machine Learning to analyze customer attributes and recommend the most suitable salon service automatically. This helps salons provide consistent and personalized service recommendations.

---

System Workflow

User enters details → Flask Web App → Machine Learning Model → Service Prediction → Result Display

---

Technologies Used

- Python
- Machine Learning (Decision Tree)
- Flask
- HTML
- CSS
- Pandas
- Scikit-learn
- Joblib
- GitHub

---

Project Structure

smartsalon-ai/
│
├── app.py
├── train_model.py
├── salon_data.csv
├── salon_model.pkl
├── le_gender.pkl
├── le_skin.pkl
├── le_hair.pkl
├── le_occasion.pkl
├── le_service.pkl
├── requirements.txt
│
├── templates/
│   └── form.html
│
└── static/
    └── style.css

---

How to Run the Project

1. Install required libraries

pip install -r requirements.txt

2. Run the Flask application

python app.py

3. Open browser and go to

http://127.0.0.1:5000

---

Machine Learning Model

The project uses a Decision Tree Classifier to predict the most suitable salon service based on customer attributes.

Input Features:

- Age
- Gender
- Skin Type
- Hair Type
- Occasion
- Budget

Output:

- Recommended Salon Service

---

Future Improvements

- Mobile application
- Online appointment booking
- Customer history tracking
- Beauty trend prediction using AI
- Multi-branch salon analytics dashboard
- Personalized product recommendations

---

Author

Sainath
SmartSalon AI – Hackathon Project

---

🔗 GitHub Repository

https://github.com/SAINATH-18/smartsalon-ai
