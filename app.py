from flask import Flask, render_template, request
from selenium import webdriver

app = Flask(__name__)
app.config["DEBUG"] = True

DRILL = 'drill'
BASS = 'bass'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_sounds():
    chrome = webdriver.Chrome()
    sound_type = request.form['sound_type']

    if sound_type == DRILL:
        chrome.get('https://www.youtube.com/watch?v=fc7XA4bo4bc&t=2683s')
    elif sound_type == BASS:
        chrome.get('https://www.youtube.com/watch?v=H8pZmH5DHnQ&t=408s')

    chrome.find_element_by_class_name('ytp-play-button').click()
    return 'Started.'


if __name__ == '__main__':
    app.run()
