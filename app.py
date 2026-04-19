from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>My Flask Website</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                padding-top: 100px;
            }
            .box {
                background: rgba(0,0,0,0.3);
                padding: 40px;
                border-radius: 20px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 My Flask Website</h1>
            <p>Deployed successfully on Railway</p>
            <h3>Welcome!</h3>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
