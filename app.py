from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Flask App</title>
        <style>
            body {
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px 50px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                text-align: center;
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            }
            h1 {
                margin-bottom: 10px;
                font-size: 2.5rem;
            }
            p {
                font-size: 1.2rem;
                margin-top: 0;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 CI/CD Successfully Deployed</h1>
            <p>Flask App running smoothly with Docker & AWS EC2!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
