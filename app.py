#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

from camera_opencv import Camera

start_ngrok_v = True

def start_ngrok():
    from pyngrok import ngrok

    url  = ngrok.connect(5000)
    print(" * Tunnel URL: ", url)



app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if start_ngrok_v == True:
    start_ngrok()

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
