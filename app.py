from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bangalru,India",
        "salary": "#250,000,00"
    },
    {
        "id": 2,
        "title": "Data Scietist",
        "location": "Delhi,India",
        "salary": "#150,000,00"
    },
    {
        "id": 3,
        "title": "Frontend Engineering",
        "location": "Remote",
        "salary": "#200,000,00"
    },
    {
        "id": 4,
        "title": "Backend Engineering",
        "location": "Lagos,Nigeria",
        "salary": "#250,000,00"
    },
]


@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)


@app.route("/members")
def welcome():
    return "hello members"


if __name__ == "__main__":
    app.run(debug=True)
