from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "/static/gifs/cat1.gif",
    "/static/gifs/cat2.gif",
    "/static/gifs/cat3.gif",
    "/static/gifs/cat4.gif",
    "/static/gifs/cat5.gif",
    "/static/gifs/cat6.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")