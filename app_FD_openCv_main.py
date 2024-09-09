from flask import Flask, render_template, Response, redirect, url_for, request
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER_IMAGES = 'static/images'
app.config['UPLOAD_FOLDER_IMAGES'] = UPLOAD_FOLDER_IMAGES

if not os.path.exists(UPLOAD_FOLDER_IMAGES):
    os.makedirs(UPLOAD_FOLDER_IMAGES)

camera = None

# Initialize the camera
def get_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
    return camera

# Release the camera
def release_camera():
    global camera
    if camera is not None and camera.isOpened():
        camera.release()
        camera = None

# Generate video frames with face and eye detection
def gen_frames():  
    camera = get_camera()
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Face and eye detection
            detector = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.1, 7)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    images = [f for f in os.listdir(app.config['UPLOAD_FOLDER_IMAGES']) if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], f))]
    return render_template('index.html', images=images)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    camera = get_camera()
    success, frame = camera.read()
    if success:
        filename = secure_filename('image.png')
        filepath = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename)
        cv2.imwrite(filepath, frame)
    release_camera()
    return redirect(url_for('index'))

@app.route('/delete_image/<filename>', methods=['POST'])
def delete_image(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)