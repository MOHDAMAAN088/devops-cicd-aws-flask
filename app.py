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
                box-shadow: 0 0 25px rgba(255, 255, 255, 0.8);
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
                <h1>🚀 CI/CD Successfully Deployed - by Mohammad Amaan </h1>
                <p>Flask App running smoothly with Docker & AWS EC2!</p>
                <div class="github">
                    📌 GitHub: <a href="https://github.com/MOHDAMAAN088" target="_blank">MOHDAMAAN088 </a> ▶️ Youtube: <a href="https://youtu.be/dRvgnLDHHJA" target="_blank">Click here to get a Quick Explanation !</a>
                </div>
            </div>

            <div class="card">
                <h2>💡 What is DevOps?</h2>
                <p>
                    DevOps is a culture and set of practices that combines Development and Operations teams to improve collaboration, 
                    automate workflows, and deploy software faster and more reliably using CI/CD, monitoring, and automation.
                </p>
            </div>

            <div class="card">
                <h2>🛠️ DevOps Tools & Their Roles</h2>
                <ul>
                    <li><strong>GitHub:</strong> Version control and team collaboration platform.</li>
                    <li><strong>Docker:</strong> Packages applications into portable containers.</li>
                    <li><strong>AWS EC2:</strong> Cloud hosting to deploy applications at scale.</li>
                    <li><strong>GitHub Actions:</strong> Automates CI/CD pipeline for build & deployment.</li>
                    <li><strong>Flask:</strong> Lightweight Python web framework for backend apps.</li>
                    <li><strong>Nginx:</strong> Reverse proxy & load balancer for traffic handling.</li>
                </ul>
            </div>

            <div class="card">
                <h2>🎥 YouTube Explanation</h2>
                <p>
                      Watch my quick explanation on 
                    <a href="https://youtu.be/dRvgnLDHHJA" target="_blank">Click here to get a Quick Explanation !</a>.<br><br>

                    In this project, we built and deployed a Flask application using Docker containers 
                    and automated the CI/CD pipeline through GitHub Actions on AWS EC2.
                    <br><br>
                    📌 Future Plan: Add HTTPS, Domain, Monitoring 🚀
                </p>
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
