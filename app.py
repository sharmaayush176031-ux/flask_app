from flask import Flask, request

app = Flask(__name__)

# ---------------- HOME SCREEN ----------------
@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Titanic Simulator</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(135deg, #141e30, #243b55);
                color: white;
                margin: 0;
                padding: 0;
            }

            .title {
                font-size: 42px;
                margin-top: 120px;
                font-weight: bold;
            }

            .btn {
                margin-top: 40px;
                padding: 15px 30px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                background: #00c6ff;
                color: white;
                cursor: pointer;
                text-decoration: none;
                display: inline-block;
            }

            .btn:hover {
                background: #0072ff;
            }
        </style>
    </head>

    <body>

        <div class="title">🚢 Titanic Prediction Simulator</div>

        <a href="/predictor" class="btn">Enter Simulation 🚀</a>

    </body>
    </html>
    """

# ---------------- FORM ----------------
@app.route('/predictor')
def predictor():
    return """
    <html>
    <head>
        <title>Predict</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
            }

            .box {
                margin-top: 50px;
                display: inline-block;
                background: rgba(0,0,0,0.35);
                padding: 30px;
                border-radius: 15px;
                width: 350px;
            }

            input, select {
                width: 90%;
                padding: 10px;
                margin: 8px 0;
                border-radius: 8px;
                border: none;
            }

            button {
                width: 95%;
                padding: 10px;
                background: #00c6ff;
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 16px;
            }

            button:hover {
                background: #0072ff;
            }
        </style>
    </head>

    <body>

        <h1>🚢 Titanic Survival Prediction</h1>

        <div class="box">

            <form action="/predict" method="post">

                <input name="age" placeholder="Age" required><br>

                <input name="fare" placeholder="Fare" required><br>

                <select name="pclass" required>
                    <option value="">Class</option>
                    <option value="1">1st Class</option>
                    <option value="2">2nd Class</option>
                    <option value="3">3rd Class</option>
                </select><br>

                <select name="sex" required>
                    <option value="">Gender</option>
                    <option value="1">Female</option>
                    <option value="0">Male</option>
                </select><br>

                <!-- ONLY FAMILY = 1 -->
                <select name="family" required>
                    <option value="1">Alone (1)</option>
                </select><br>

                <button type="submit">Predict Survival</button>

            </form>

        </div>

    </body>
    </html>
    """

# ---------------- PREDICTION ----------------
@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])
    family = int(request.form['family'])

    score = 0

    if pclass == 1:
        score += 40
    elif pclass == 2:
        score += 20

    if sex == 1:
        score += 30

    if age < 18:
        score += 20
    elif age > 60:
        score -= 10

    if fare > 50:
        score += 10

    # family always alone (1)
    score -= 5

    if score > 100:
        score = 100
    if score < 0:
        score = 0

    result = "✅ Survived" if score >= 50 else "❌ Not Survived"

    # ---------------- RESULT UI ----------------
    return f"""
    <html>
    <head>
        <title>Result</title>
        <style>
            body {{
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding-top: 80px;
            }}

            .card {{
                background: rgba(255,255,255,0.08);
                padding: 30px;
                border-radius: 15px;
                width: 350px;
                margin: auto;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}

            .bar {{
                width: 100%;
                background: #333;
                border-radius: 10px;
                margin-top: 20px;
            }}

            .fill {{
                height: 20px;
                width: {score}%;
                background: linear-gradient(90deg, #00c6ff, #0072ff);
                border-radius: 10px;
            }}

            .btn {{
                margin-top: 20px;
                display: inline-block;
                color: #00c6ff;
                text-decoration: none;
            }}
        </style>
    </head>

    <body>

        <div class="card">

            <h1>{result}</h1>

            <h2>📊 Probability: {score}%</h2>

            <div class="bar">
                <div class="fill"></div>
            </div>

            <a class="btn" href="/">🔙 Try Again</a>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
