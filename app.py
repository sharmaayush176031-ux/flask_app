from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Flask Website</title>
        </head>
        <body style="text-align:center; font-family:Arial;">
            <h1>🚀 Welcome to My Flask App</h1>
            <p>Successfully deployed on Railway</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
