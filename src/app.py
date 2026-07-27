from flask import Flask, render_template
from api import register_api

app = Flask(__name__)

register_api(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
