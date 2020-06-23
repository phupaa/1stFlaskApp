from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://phupaapublicblob.blob.core.windows.net/public/view1.jpg",
    "https://phupaapublicblob.blob.core.windows.net/public/view2.jpg",
    "https://phupaapublicblob.blob.core.windows.net/public/view3.jpg.jpg",
    "https://phupaapublicblob.blob.core.windows.net/public/view4.jpg",
    "https://phupaapublicblob.blob.core.windows.net/public/view5.jpg",
    "https://phupaapublicblob.blob.core.windows.net/public/view6.jpg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")