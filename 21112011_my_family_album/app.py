from flask import Flask, render_template

app = Flask(__name__)

# Sample data for family photos
family_photos = [
    {"title": "Friends are Family!!", "image": "/static/images/GroupPhoto.jpeg"},
    {"title": "At the Top!!", "image": "/static/images/IMG_7429.JPG"},
    {"title": "My World!!", "image": "/static/images/420100.jpg"}
    # Add more photos and details here
]

@app.route('/')
def index():
    return render_template('index.html', photos=family_photos)

if __name__ == '__main__':
    app.run(debug=True)
