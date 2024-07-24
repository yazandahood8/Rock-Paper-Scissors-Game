# Rock-Paper-Scissors Game with Hand Detection

This project demonstrates a Rock-Paper-Scissors game using real-time hand gesture recognition with OpenCV and MediaPipe. The application captures video from the webcam, detects hand gestures to determine the number of fingers, and displays corresponding images based on the game outcome.

## Features
- Real-time hand gesture recognition
- Rock-Paper-Scissors game logic
- Displays images based on the hand gesture and game result
- Stacks video frame and image frame for visual output

## Prerequisites
- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yazandahood8/Rock-Paper-Scissors-Game
    ```

2. Navigate to the project directory:

    ```bash
    cd Rock-Paper-Scissors-Game
    ```

3. Install the required packages:

    ```bash
    pip install opencv-python mediapipe numpy
    ```

## Usage
1. Prepare the required image files in the project directory:
    - `empty.png` (default image when no hand is detected)
    - `image1.png` (image for specific finger count)
    - `image2.png` (image for specific finger count)
    - `image3.png` (image for specific finger count)
    - `win.png` (image displayed for winning condition)
    - `draw.png` (image displayed for draw condition)
    - `lose.png` (image displayed for losing condition)

2. Run the script:

    ```bash
    python finger_counter.py
    ```

   The application will open a window showing the video feed from your webcam with overlays based on detected hand gestures. Press 'q' to quit the application.

## Code Explanation
- `count_fingers(hand_landmarks)`: Counts the number of fingers extended based on hand landmarks.
- `load_and_resize_image(image_path, size)`: Loads and resizes an image from the specified path.
- `create_image_frame(image1, image2, image3)`: Stacks three images to create a frame for display.
- `main()`: Captures video from the webcam, processes hand gestures, updates image displays, and combines video and image frames for output.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
