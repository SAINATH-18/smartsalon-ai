import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("salon_data.csv")

# Convert text to numbers
le_gender = LabelEncoder()
le_skin = LabelEncoder()
le_hair = LabelEncoder()
le_occasion = LabelEncoder()
le_service = LabelEncoder()

data['gender'] = le_gender.fit_transform(data['gender'])
data['skin_type'] = le_skin.fit_transform(data['skin_type'])
data['hair_type'] = le_hair.fit_transform(data['hair_type'])
data['occasion'] = le_occasion.fit_transform(data['occasion'])
data['service'] = le_service.fit_transform(data['service'])

# Features and target
X = data[['age','gender','skin_type','hair_type','occasion','budget']]
y = data['service']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, "salon_model.pkl")
joblib.dump(le_gender, "le_gender.pkl")
joblib.dump(le_skin, "le_skin.pkl")
joblib.dump(le_hair, "le_hair.pkl")
joblib.dump(le_occasion, "le_occasion.pkl")
joblib.dump(le_service, "le_service.pkl")

print("Model trained and saved!")