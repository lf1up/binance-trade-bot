import os
import logging
from flask import Flask, redirect, request

# Create Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

@app.before_request
def log_request():
    logger.info(f"Request from {request.remote_addr} to {request.path} with method {request.method}")

@app.route("/")
def redirect_to_google():
    return redirect("https://www.google.com", code=302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Ensure compatibility with Heroku
    app.run(host="0.0.0.0", port=port, debug=False)
