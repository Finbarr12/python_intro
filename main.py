# Integrate HTML with flask
# HTTP GET AND POST

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/members")
def welcome():
    return "hello members"


@app.route("/sucess/<int:score>")
def success(score):
    return "<html><body><h1>The person has passed and the marks is</h1></body></html>" + str(score)


@app.route("/fail/<int:score>")
def failure(score):
    return "The person has failed and the marks is " + str(score)

# result checker


@app.route("/result/<int:marks>")
def results(marks):
    result = ''
    if marks < 50:
        result = "failure"
    else:
        result = "success"

    return redirect(url_for(result, score=marks))

# Result checker
# @app.route("/submit",methods = ['POST','GET'])

# def submit():


if __name__ == "__main__":
    app.run(debug=True)
