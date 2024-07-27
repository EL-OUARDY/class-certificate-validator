from flask import Flask, render_template, abort
from dotenv import load_dotenv
import os
import csv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/validate")
def validate():
    return render_template("validate.html")


@app.route("/certificate/<certificate_id>")
def certificate(certificate_id):
    csv_file = "./data/students.csv"
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("code") == certificate_id:
                return render_template("certificate.html", student=row)

    abort(404)


@app.route("/curriculum")
def curriculum():
    return render_template("curriculum.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Get the debug value from the environment variable
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)
