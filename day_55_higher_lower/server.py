import random

from flask import Flask

app = Flask(__name__)

number = random.randint(1, 9)


@app.route("/")
def welcome():
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers" />'


@app.route("/<int:guess>")
def respond(guess):
    if guess == number:
        return "<h1 style='color: green'>You found me!</h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="cute dog" />'
    elif guess > number:
        return '<h1 style="color: blue">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="cute dog" />'
    else:
        return "<h1 style='color: brown'>Too low, try again!</h1>" \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="cute dog" />'


if __name__ == "__main__":
    app.run(debug=True)
