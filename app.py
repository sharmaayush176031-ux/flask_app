from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Titanic Survival Prediction</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: #0f172a;
                color: white;
                padding: 50px;
            }
            input, button {
                padding: 10px;
                margin: 5px;
                border-radius: 5px;
                border: none;
            }
            button {
                background: #38bdf8;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>🚢 Titanic Survival Prediction</h1>

        <form action="/predict" method="post">
            <input name="age" placeholder="Age" required><br>
            <input name="fare" placeholder="Fare" required><br>
            <input name="pclass" placeholder="Class (1/2/3)" required><br>
            <button type="submit">Predict</button>
        </form>
    </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    pclass = int(request.form['pclass'])

    # SIMPLE RULE-BASED MODEL (no ML file needed)
    if pclass == 1 and fare > 50 and age < 50:
        result = "✅ Survived"
    else:
        result = "❌ Not Survived"

    return f"""
    <h1>{result}</h1>
    <br><a href='/'>Go Back</a>
    """

if __name__ == "__main__":
    app.run()
