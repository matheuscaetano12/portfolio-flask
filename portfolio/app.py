import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    with open("data/data.json","r", encoding="utf-8") as f:
        data = json.load(f)
    return render_template("index.html", bio=data["bio"])

if __name__ == "__main__":
    app.run(debug=True)