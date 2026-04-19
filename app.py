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
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                margin: 0;
                padding: 0;
            }

            h1 {
                margin-top: 20px;
            }

            .intro {
                margin-top: 10px;
                font-size: 18px;
                opacity: 0.9;
            }

            .box {
                margin-top: 30px;
                display: inline-block;
                background: rgba(0,0,0,0.35);
                padding: 30px;
                border-radius: 15px;
                width: 350px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }

            input, select {
                width: 90%;
                padding: 10px;
                margin: 8px 0;
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
        </style>
    </head>

    <body>

        <h1>🚢 Titanic Survival Prediction</h1>

        <div class="intro">
            You are going to predict whether a passenger survived the Titanic disaster based on input details.
        </div>

        <div class="box">

            <form action="/predict" method="post">

                <input name="age" placeholder="Age" required><br>

                <input name="fare" placeholder="Fare" required><br>

                <select name="pclass" required>
                    <option value="">Select Class</option>
                    <option value="1">1st Class (Rich)</option>
                    <option value="2">2nd Class (Middle)</option>
                    <option value="3">3rd Class (Low)</option>
                </select><br>

                <select name="sex" required>
                    <option value="">Select Gender</option>
                    <option value="1">Female</option>
                    <option value="0">Male</option>
                </select><br>

                <select name="family" required>
                    <option value="">Family Size</option>
                    <option value="0">0 (Alone)</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4+</option>
                </select><br>

                <button type="submit">Predict Survival</button>

            </form>

        </div>

    </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])
    family = int(request.form['family'])

    score = 0

    # Class effect
    if pclass == 1:
        score += 40
    elif pclass == 2:
        score += 20

    # Gender effect
    if sex == 1:
        score += 30  # female advantage

    # Age effect
    if age < 18:
        score += 20
    elif age > 60:
        score -= 10

    # Fare effect
    if fare > 50:
        score += 10

    # Family effect
    if family == 0:
        score -= 5
    elif family in [1, 2]:
        score += 10
    else:
        score += 5

    if score > 100:
        score = 100
    if score < 0:
        score = 0

    result = "✅ Survived" if score >= 50 else "❌ Not Survived"

    return f"""
    <html>
    <body style="text-align:center; font-family:Arial; background:#0f172a; color:white; padding-top:100px;">

        <h1>{result}</h1>
        <h2>📊 Survival Score: {score}%</h2>

        <br><br>
        <a href="/" style="color:#00c6ff; font-size:18px;">🔙 Try Again</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
