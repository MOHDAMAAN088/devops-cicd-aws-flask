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
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px 50px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                text-align: center;
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
                max-width: 900px;
            }
            h1 {
                margin-bottom: 10px;
                font-size: 2.5rem;
            }
            p, li {
                font-size: 1.1rem;
                margin-top: 5px;
            }
            .github {
                margin-top: 20px;
                font-size: 1.1rem;
                font-weight: bold;
            }
            .section-title {
                margin-top: 25px;
                font-size: 1.8rem;
                font-weight: bold;
            }
            ul {
                text-align: left;
                margin: 10px auto;
                max-width: 650px;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 CI/CD Successfully Deployed - by Mohammad Amaan</h1>
            <p>Flask App running smoothly with Docker & AWS EC2!</p>
            
            <div class="github">
                📌 GitHub: <a href="https://github.com/MOHDAMAAN088" target="_blank" style="color:white;">MOHDAMAAN088</a>
            </div>

            <div class="section-title">💡 What is DevOps?</div>
            <p>
                DevOps is a culture and set of practices that improves collaboration between 
                development and operations teams by using automation, continuous integration, 
                and continuous delivery to build, test, and deploy software faster and more reliably.
            </p>

            <div class="section-title">🛠️ DevOps Tools with Their Roles</div>
            <ul>
                <li><strong>GitHub:</strong> A cloud-based version control system used for storing code, collaborating with teams, tracking changes, and managing projects using Git repositories.</li>
                <li><strong>Docker:</strong> A containerization platform that packages applications with their dependencies, allowing them to run consistently across different environments (development, testing, production).</li>
                <li><strong>AWS EC2:</strong> Elastic Compute Cloud provides scalable virtual servers in the AWS cloud for hosting and deploying applications, ensuring global accessibility and high availability.</li>
                <li><strong>GitHub Actions:</strong> An automation tool that builds CI/CD pipelines directly from GitHub repositories, enabling automatic testing, building, and deployment after every code commit.</li>
                <li><strong>Flask:</strong> A lightweight Python web framework used to build web applications quickly, commonly used in backend development and testing microservices in DevOps.</li>
                <li><strong>Nginx:</strong> A powerful web server and reverse proxy used for load balancing, improving performance, and securely routing traffic to applications.</li>
                <li><strong>Jenkins (Optional):</strong> An automation server widely used in DevOps for building advanced CI/CD pipelines and integrating multiple tools with plugins.</li>
            </ul>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
