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
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                margin: 0;
                padding: 0;
            }

            .hero {
                margin-top: 40px;
            }

            .title {
                font-size: 40px;
                font-weight: bold;
                margin-top: 20px;
            }

            .subtitle {
                font-size: 18px;
                margin-top: 10px;
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
                padding: 12px;
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

            .footer-text {
                margin-top: 20px;
                font-size: 14px;
                opacity: 0.7;
            }
        </style>
    </head>

    <body>

        <div class="hero">
            <div class="title">🚢 Titanic Survival Prediction</div>
            <div class="subtitle">Enter details to predict whether a passenger survived or not</div>
        </div>

        <div class="box">

            <form action="/predict" method="post">

                <input name="age" placeholder="Enter Age" required><br>

                <input name="fare" placeholder="Enter Fare" required><br>

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

                <button type="submit">Enter to Predict Titanic 🚢</button>

            </form>

        </div>

        <div class="footer-text">
            Built with Flask • AI Style Project
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
        score += 30

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
