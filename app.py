from flask import Flask, request

app = Flask(__name__)

# ---------------- START PAGE ----------------
@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Titanic Simulator</title>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                text-align: center;
                color: white;

                /* Titanic-style ocean background */
                background: url('https://images.unsplash.com/photo-1500375592092-40eb2168fd21?auto=format&fit=crop&w=1600&q=80');
                background-size: cover;
                background-position: center;
            }

            .overlay {
                background: rgba(0,0,0,0.6);
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .title {
                font-size: 50px;
                font-weight: bold;
            }

            .subtitle {
                font-size: 18px;
                margin-top: 10px;
                opacity: 0.9;
            }

            .btn {
                margin-top: 40px;
                padding: 15px 35px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                background: #00c6ff;
                color: white;
                text-decoration: none;
                transition: 0.3s;
            }

            .btn:hover {
                background: #0072ff;
                transform: scale(1.05);
            }
        </style>
    </head>

    <body>

        <div class="overlay">

            <div class="title">🚢 Titanic Prediction Simulator</div>

            <div class="subtitle">
                Enter passenger details and predict survival probability
            </div>

            <a class="btn" href="/predictor">Enter 🚀</a>

        </div>

    </body>
    </html>
    """

# ---------------- FORM PAGE ----------------
@app.route('/predictor')
def predictor():
    return """
    <html>
    <head>
        <title>Prediction</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(135deg, #141e30, #243b55);
                color: white;
            }

            .box {
                margin-top: 40px;
                display: inline-block;
                background: rgba(255,255,255,0.08);
                padding: 30px;
                border-radius: 15px;
                width: 350px;
                backdrop-filter: blur(10px);
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
            }

            button:hover {
                background: #0072ff;
            }

            .note {
                font-size: 12px;
                opacity: 0.8;
                margin-bottom: 10px;
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

                <!-- FAMILY -->
                <select name="family" required>
                    <option value="">Family Size</option>
                    <option value="1">1 (Alone)</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4+</option>
                </select>

                <div class="note">
                    * 1 means Alone
                </div>

                <button type="submit">Enter Prediction 🚢</button>

            </form>

        </div>

    </body>
    </html>
    """

# ---------------- RESULT PAGE ----------------
@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])
    family = int(request.form['family'])

    score = 0

    # class impact
    if pclass == 1:
        score += 40
    elif pclass == 2:
        score += 20

    # gender impact
    if sex == 1:
        score += 30

    # age impact
    if age < 18:
        score += 20
    elif age > 60:
        score -= 10

    # fare impact
    if fare > 50:
        score += 10

    # family impact
    if family == 1:
        score -= 5   # alone
    elif family == 2:
        score += 10
    elif family == 3:
        score += 8
    else:
        score += 5

    if score > 100:
        score = 100
    if score < 0:
        score = 0

    result = "✅ Survived" if score >= 50 else "❌ Not Survived"

    return f"""
    <html>
    <head>
        <title>Result</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                background: #0f172a;
                color: white;
                padding-top: 80px;
            }}

            .card {{
                background: rgba(255,255,255,0.08);
                width: 350px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
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

            a {{
                display: inline-block;
                margin-top: 20px;
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

            <a href="/">🔙 Back to Home</a>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
