from flask import Flask, render_template, request, redirect, url_for
import os
import picamera
import time
import json


app = Flask(__name__)
path = os.getcwd()

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/welcome/', methods=['POST', 'GET'])
def camera():
    if request.method == 'POST':
        #name = request.form['username']
        #with picamera.PiCamera() as camera:
            #time.sleep(4)
            #camera.capture(path + '/static/profilePics/' + name + '.jpg')
        return redirect('/')
    else:
        return render_template('welcome_1.html')

@app.route('/profile/')
def profile():
    imgs = os.listdir(path + '/static/profilePics/')
    data = json.dumps(imgs)
    print imgs
    return render_template('profile.html', data=data)

@app.route('/outOfOrder')
def shitHappens():
    return 'out of order :('
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


