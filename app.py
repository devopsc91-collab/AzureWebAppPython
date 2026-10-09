```python
from flask import Flask, render_template, jsonify
import os
import platform
from datetime import datetime, timezone

app = Flask(__name__)

# Application configuration
APP_NAME = os.environ.get("APP_NAME", "Cloud DevOps Web App")
APP_VERSION = "2.0.0"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")


@app.route("/")
def home():
    return render_template("index.html")


# Health check endpoint
@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is running successfully",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


# Application information
@app.route("/api/info")
def info():
    return jsonify({
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "framework": "Flask",
        "python_version": platform.python_version(),
        "environment": ENVIRONMENT
    }), 200


# Welcome API
@app.route("/api/welcome")
def welcome():
    return jsonify({
        "message": "Welcome to the Cloud DevOps Web Application!",
        "features": [
            "Flask web server",
            "REST API",
            "Health monitoring",
            "Azure deployment ready"
        ]
    }), 200


# Application readiness check
@app.route("/api/ready")
def ready():
    return jsonify({
        "status": "ready",
        "message": "Application is ready to receive requests"
    }), 200


# Handle unknown URLs
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "The requested API endpoint does not exist"
    }), 404


# Handle unexpected server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred"
    }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=ENVIRONMENT == "development"
    )
```
