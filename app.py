from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

# Load models
rf_model = pickle.load(open("model_rf.pkl", "rb"))
nb_model = pickle.load(open("model_nb.pkl", "rb"))

# Home page
@app.route('/')
def home():
    return """
    <html>
    <body style="text-align:center;font-family:Arial;background:#0f172a;color:white;">
        <h1>🚢 Titanic Survival Predictor</h1>
        <a href="/predictor" style="color:#00c6ff;font-size:20px;">Enter Simulation</a>
    </body>
    </html>
    """

# Input page
@app.route('/predictor')
def predictor():
    return """
    <html>
    <body style="text-align:center;font-family:Arial;background:#1e3c72;color:white;">

        <h1>Enter Passenger Details</h1>

        <form action="/predict" method="post">

            <input name="age" placeholder="Age" required><br><br>
            <input name="fare" placeholder="Fare" required><br><br>

            <select name="pclass">
                <option value="1">1st Class</option>
                <option value="2">2nd Class</option>
                <option value="3">3rd Class</option>
            </select><br><br>

            <select name="sex">
                <option value="1">Male</option>
                <option value="0">Female</option>
            </select><br><br>

            <button type="submit">Predict</button>

        </form>

    </body>
    </html>
    """

# Prediction
@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])

    data = np.array([[pclass, sex, age, fare]])

    rf_pred = rf_model.predict(data)[0]
    nb_pred = nb_model.predict(data)[0]

    result = "Survived" if rf_pred == 1 else "Not Survived"

    return f"""
    <html>
    <body style="text-align:center;font-family:Arial;background:#111827;color:white;padding-top:100px;">

        <h1>🚢 Result: {result}</h1>

        <h2>Random Forest: {rf_pred}</h2>
        <h2>Naive Bayes: {nb_pred}</h2>

        <br><br>
        <a href="/" style="color:#00c6ff;">Back Home</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
