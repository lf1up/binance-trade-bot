from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def redirect_to_google():
    return redirect("https://www.google.com", code=302)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Ensure compatibility with Heroku
    app.run(host="0.0.0.0", port=port)