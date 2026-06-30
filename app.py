from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Dockerized Web Application</h1>
    <p>This Python Flask app is running inside a Docker container.</p>
    <p>Built as part of my DevOps and Cloud portfolio.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)