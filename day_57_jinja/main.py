from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", post1=Post(1), post2=Post(2), post3=Post(3))


@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/post/<int:post_id>')
def read_post(post_id):
    return render_template("post.html", post=Post(post_id))


if __name__ == "__main__":
    app.run(debug=True)
