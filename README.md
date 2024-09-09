# Flask Face and eye Detection App

This is a Flask web application that streams video from a webcam and detects faces and eyes in real-time using OpenCV. Users can capture and save images from the video feed, and the saved images are displayed in a gallery with the option to delete them.

## Features

- **Live Video Streaming**: Streams real-time video from the webcam.
- **Face and Eye Detection**: Uses Haar Cascade Classifiers to detect faces and eyes.
- **Capture Images**: Allows users to capture frames from the live feed and store them.
- **Image Gallery**: Displays captured images with the option to delete them.
- **Responsive Design**: Styled using Bootstrap for a clean and responsive user interface.

## Technologies Used

- **Flask**: Python web framework.
- **OpenCV**: Library for computer vision.
- **HTML/CSS**: Frontend design.
- **Bootstrap**: For responsive design.

## Prerequisites

Before running the project, you will need:

- Python 3.x
- OpenCV (`cv2`)
- Flask
- Bootstrap (linked via CDN in the HTML)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # OR
    venv\Scripts\activate  # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install OpenCV if it’s not in the requirements file:

    ```bash
    pip install opencv-python
    ```

5. Create the necessary directories for storing images:

    ```bash
    mkdir -p static/images
    ```

## Running the Application

1. To start the Flask app, run:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to:

    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

```bash
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/
│   └── images/             # Directory for captured images
├── templates/
│   └── index.html          # HTML template for the app
└── README.md               # This documentation file
```

## 🎥 Usage

1. **Start the Camera**: Click the “Start Camera” button to begin streaming from the webcam.
2. **Stop the Camera**: Click the “Stop Camera” button to stop the webcam feed.
3. **Capture Image**: Click the “Capture Image” button to take a snapshot and save it as a PNG file.
4. **Start Recording**: Click the “Start Recording” button to begin recording a video.
5. **Stop Recording**: Click the “Stop Recording” button to stop the video recording and save it as an MP4 file.

## 📷 Gallery

- **View Images**: Captured images will appear in the gallery on the right side of the page.
- **View Videos**: Recorded videos are also displayed in the gallery and can be played directly.
- **Delete Media**: Use the “Delete” button next to images and videos to remove them from the gallery.

## 🖼️ Screenshots

<img width="1440" alt="Screenshot 2024-09-09 at 11 13 04 PM" src="https://github.com/user-attachments/assets/a84ec8f3-c76d-4a33-b18d-495cbb8bc5d5">

<img width="1440" alt="Screenshot 2024-09-09 at 11 13 04 PM" src="https://github.com/user-attachments/assets/8edafc97-4f68-4b19-8978-f88177f8101e">

## Face and Eye Detection

The application uses Haar Cascade Classifiers to detect faces and eyes in real-time. You can download the necessary XML files from the OpenCV GitHub repository.

- `haarcascade_frontalface_default.xml`
- `haarcascade_eye.xml`

Make sure these XML files are placed in the `Haarcascades` folder in the project directory.

## Usage

- **Live Video Stream**: View real-time video from your webcam.
- **Capture Image**: Click the “Capture Image” button to take a snapshot of the live stream.
- **Image Gallery**: Captured images appear on the right side in the gallery. Hover over images to view or delete them.

## Gallery

Captured images are stored in the `static/images/` directory and displayed in the gallery section on the web page. The gallery is interactive and allows users to delete images.

## Troubleshooting

- **Camera Access Issues**: If the webcam isn’t accessible, ensure that no other application is using the camera.
- **Face/Eye Detection Issues**: Verify that the Haar Cascade XML files are in the correct directory.

## License

This project is licensed under the MIT License.
