from flask import Flask

app = Flask(__name__)


def make_bold(fun):
    def wrapper():
        text = fun()
        return f"<b>{text}</b>"

    return wrapper


@app.route("/")  # url adres/ olduğunda yani ana ekrandaysan body içine hello world döndür.
def hello_world():
    return "<p>Hello, World!</p>"


# eğer sitede /bye sayfasına gidersen yani incoming url /bye ise h2 bye döndür.
@app.route("/bye")
@make_bold
def bye():
    return "<p>Bye!<p>"


@app.route("/username/<name>")
def greet(name):
    return f"<h2 style='color: green'>Hello {name}! What's up!"


# You can specify variable type too like this:
@app.route("/username/<string:name>/<int:age>")
def greeting(name, age):
    return f"<h2 style='color: green'>Hello {name}! You're {age} years old!"


# Eğer yukarıdan biri olmazsa en son bu çalışır.
# You can parse the path like this because if you parse it with string it doesn't include the '/'
@app.route("/<path:yol>")
def print_path(yol):
    return f"<p>{yol}</p>"


# this allows us to run the server with pycharm run and stop buttons. Not to deal with terminal.
if __name__ == "__main__":
    app.run(debug=True)
