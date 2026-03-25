from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load("salon_model.pkl")
le_gender = joblib.load("le_gender.pkl")
le_skin = joblib.load("le_skin.pkl")
le_hair = joblib.load("le_hair.pkl")
le_occasion = joblib.load("le_occasion.pkl")
le_service = joblib.load("le_service.pkl")
 
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        age = int(request.form["age"])
        gender = le_gender.transform([request.form["gender"]])[0]
        skin = le_skin.transform([request.form["skin"]])[0]
        hair = le_hair.transform([request.form["hair"]])[0]
        occasion = le_occasion.transform([request.form["occasion"]])[0]
        budget = int(request.form["budget"])

        prediction = model.predict([[age, gender, skin, hair, occasion, budget]])
        service = le_service.inverse_transform(prediction)[0]

        return f"<h2>Recommended Service: {service}</h2>"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)