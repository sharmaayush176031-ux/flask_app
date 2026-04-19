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

            .box {
                margin-top: 50px;
                display: inline-block;
                background: rgba(0,0,0,0.3);
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
            }

            button:hover {
                background: #0072ff;
            }

            .info {
                margin-top: 30px;
                background: rgba(0,0,0,0.2);
                padding: 20px;
                width: 70%;
                margin-left: auto;
                margin-right: auto;
                border-radius: 10px;
            }
        </style>
    </head>

    <body>

        <h1>🚢 Titanic Survival Prediction</h1>

        <div class="box">
            <form action="/predict" method="post">

                <input name="age" placeholder="Age" required><br>

                <input name="fare" placeholder="Fare" required><br>

                <input name="pclass" placeholder="Class (1/2/3)" required><br>

                <select name="sex" required>
                    <option value="1">Female</option>
                    <option value="0">Male</option>
                </select><br>

                <input name="sibsp" placeholder="Siblings/Spouse (SibSp)" required><br>

                <input name="parch" placeholder="Parents/Children (Parch)" required><br>

                <button type="submit">Predict Survival</button>

            </form>
        </div>

        <div class="info">
            <h2>📘 Feature Meaning</h2>
            <p><b>Age:</b> Age of passenger</p>
            <p><b>Fare:</b> Ticket price paid</p>
            <p><b>Class:</b> 1 = Rich, 2 = Middle, 3 = Low</p>
            <p><b>Sex:</b> Gender of passenger</p>
            <p><b>SibSp:</b> Siblings / spouse aboard</p>
            <p><b>Parch:</b> Parents / children aboard</p>
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
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])

    score = 0

    # Class effect
    if pclass == 1:
        score += 40
    elif pclass == 2:
        score += 20

    # Gender effect
    if sex == 1:
        score += 30  # female higher chance

    # Age effect
    if age < 18:
        score += 20
    elif age > 60:
        score -= 10

    # Fare effect
    if fare > 50:
        score += 10

    # Family effect
    if sibsp > 0:
        score += 5
    if parch > 0:
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
        <a href="/" style="color:#00c6ff;">🔙 Try Again</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
