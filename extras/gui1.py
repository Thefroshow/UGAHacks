'''
from Tkinter import *
import cv
#create the window
root = Tk()

#modify root window
root.title("Sellerfai")
root.geometry("700x900")

app = Frame(root)
app.grid()

button1 = Button(app, text = "Take Picture")
button1.grid()
#kick off the main loop
root.mainloop()
'''
#!/usr/bin/env python
from flask import Flask, render_template, Response
#from camera import Camera
from time import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
class Camera(object):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frames[int(time()) % 3]