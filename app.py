from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello worldgdggdsss"


@app.route("/members")
def welcome():
    return "hello members"


@app.route("/sucess/<int:score>")
def success(score):
    return "The person has passed and the marks is " + str(score)


@app.route("/fail/<int:score>")
def failure(score):
    return "The person has failed and the marks is " + str(score)

# result checker


@app.route("/result/<int:score>")
def results(score):
    result = ''
    if score < 50:
        result = "fail"
    else:
        result = "success"

        return result


if __name__ == "__main__":
    app.run(debug=True)
