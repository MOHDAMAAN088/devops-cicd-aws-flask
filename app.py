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
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }
            .container {
                text-align: center;
                max-width: 900px;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                padding: 25px 40px;
                border-radius: 15px;
                backdrop-filter: blur(12px);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
                transition: transform 0.3s, box-shadow 0.3s;
            }
            .card:hover {
                transform: scale(1.03);
                box-shadow: 0 0 25px rgba(255, 255, 255, 0.7);
            }
            h1 {
                margin-bottom: 10px;
                font-size: 2.5rem;
            }
            h2 {
                font-size: 1.8rem;
                margin-bottom: 10px;
            }
            p, li {
                font-size: 1.1rem;
                line-height: 1.6;
            }
            ul {
                text-align: left;
                margin: 10px auto;
                max-width: 650px;
            }
            .github {
                margin-top: 20px;
                font-size: 1.1rem;
                font-weight: bold;
            }
            a {
                color: white;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">

            <div class="card">
                <h1>🚀 CI/CD Successfully Deployed - by Mohammad Amaan</h1>
                <p>Flask App running smoothly with Docker & AWS EC2!</p>
                <div class="github">
                    📌 GitHub: <a href="https://github.com/MOHDAMAAN088" target="_blank">MOHDAMAAN088</a>
                </div>
            </div>

            <div class="card">
                <h2>💡 What is DevOps?</h2>
                <p>
                    DevOps is a cultural and technical practice that integrates Development and Operations teams
                    to improve collaboration, automate workflows, and accelerate software delivery with higher
                    reliability and efficiency. It focuses on Continuous Integration, Continuous Delivery (CI/CD),
                    automation, and monitoring.
                </p>
            </div>

            <div class="card">
                <h2>🛠️ DevOps Tools & Their Roles</h2>
                <ul>
                    <li><strong>GitHub:</strong> Used for version control, source code management, and team collaboration.</li>
                    <li><strong>Docker:</strong> Containerization tool that packages apps with their dependencies to run anywhere.</li>
                    <li><strong>AWS EC2:</strong> Cloud platform that provides virtual servers to host and deploy applications.</li>
                    <li><strong>GitHub Actions:</strong> Automates CI/CD pipelines to build, test, and deploy applications.</li>
                    <li><strong>Flask:</strong> Python web framework used to build lightweight web applications.</li>
                    <li><strong>Nginx:</strong> Web server and reverse proxy for load balancing and request handling.</li>
                </ul>
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
