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
                margin: 0;
                font-family: Arial;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }

            .container {
                margin-top: 60px;
            }

            .card {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                width: 350px;
                margin: auto;
                border-radius: 15px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
                backdrop-filter: blur(10px);
            }

            input {
                width: 90%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 8px;
                border: none;
                outline: none;
            }

            button {
                width: 95%;
                padding: 10px;
                background: #00c6ff;
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background: #0072ff;
            }

            .info {
                margin-top: 40px;
                padding: 20px;
                background: rgba(0,0,0,0.3);
                width: 60%;
                margin-left: auto;
                margin-right: auto;
                border-radius: 10px;
            }

            h1 {
                margin-top: 30px;
            }
        </style>
    </head>

    <body>

        <h1>🚢 Titanic Survival Prediction</h1>

        <div class="container">
            <div class="card">
                <form action="/predict" method="post">
                    <input name="age" placeholder="Enter Age" required><br>
                    <input name="fare" placeholder="Enter Fare" required><br>
                    <input name="pclass" placeholder="Class (1 / 2 / 3)" required><br>
                    <button type="submit">Predict Survival</button>
                </form>
            </div>
        </div>

        <div class="info">
            <h2>📘 What do these inputs mean?</h2>
            <p><b>Age:</b> Age of the passenger on the Titanic</p>
            <p><b>Fare:</b> Ticket price paid by passenger</p>
            <p><b>Class:</b> Passenger class (1 = Rich, 2 = Middle, 3 = Low)</p>
        </div>

    </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    pclass = int(request.form['pclass'])

    # Simple probability logic (demo ML style)
    probability = 0

    if pclass == 1:
        probability += 50
    if fare > 50:
        probability += 30
    if age < 50:
        probability += 20

    if probability > 100:
        probability = 100

    if probability >= 50:
        result = "✅ Survived"
    else:
        result = "❌ Not Survived"

    return f"""
    <html>
    <body style="text-align:center; font-family:Arial; background:#0f172a; color:white; padding-top:100px;">
        <h1>{result}</h1>
        <h2>📊 Survival Probability: {probability}%</h2>
        <a href="/" style="color:#00c6ff;">🔙 Go Back</a>
    </body>
    </html>
    """
