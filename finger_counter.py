import cv2
import mediapipe as mp
import numpy as np

def count_fingers(hand_landmarks):
    finger_count = 0

    # Thumb
    if hand_landmarks[4].x < hand_landmarks[3].x:
        finger_count += 1

    # Index finger
    if hand_landmarks[8].y < hand_landmarks[6].y:
        finger_count += 1

    # Middle finger
    if hand_landmarks[12].y < hand_landmarks[10].y:
        finger_count += 1

    # Ring finger
    if hand_landmarks[16].y < hand_landmarks[14].y:
        finger_count += 1

    # Pinky finger
    if hand_landmarks[20].y < hand_landmarks[18].y:
        finger_count += 1

    return finger_count

def load_and_resize_image(image_path, size):
    image = cv2.imread(image_path)
    return cv2.resize(image, size)

def create_image_frame(image1, image2, image3):
    # Stack two images horizontally
    top_row = np.hstack((image1, image2))

    # Stack top row and bottom image vertically
    image_frame = np.vstack((top_row, image3))

    return image_frame

def main():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils
    strings=["image1.png","image2.png","image3.png"]
    i=0
    isplay=False
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if isplay==False:
            i=i+1
       # if i>2:
        #    i=0

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image with mediapipe hands
        results = hands.process(rgb_frame)

        # Default images
        image1 = load_and_resize_image('empty.png', (160, 120))
        image2 = load_and_resize_image(strings[i%3], (160, 120))
        image3 = load_and_resize_image('empty.png', (320, 120))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Count fingers
                finger_count = count_fingers(hand_landmarks.landmark)
                isplay=True
                # Choose the appropriate image based on the finger count
                if finger_count > 3:
                    image1 = load_and_resize_image('image2.png', (160, 120))
                    if i%3==0:
                        image3= load_and_resize_image('win.png', (320, 120))
                    elif i%3==1:
                        image3= load_and_resize_image('draw.png', (320, 120))
                    else:
                        image3= load_and_resize_image('lose.png', (320, 120))


                    
                elif finger_count == 0:
                    image1 = load_and_resize_image('image1.png', (160, 120))
                    if i%3==0:
                        image3= load_and_resize_image('draw.png', (320, 120))
                    elif i%3==1:
                        image3= load_and_resize_image('lose.png', (320, 120))
                    else:
                        image3= load_and_resize_image('win.png', (320, 120))
                else:
                    image1 = load_and_resize_image('image3.png', (160, 120))
                    if i%3==0:
                        image3= load_and_resize_image('lose.png', (320, 120))
                    elif i%3==1:
                        image3= load_and_resize_image('win.png', (320, 120))
                    else:
                        image3= load_and_resize_image('draw.png', (320, 120))

                # Create the image frame
                image_frame = create_image_frame(image1, image2, image3)

                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

              
        else:
            # Use the empty image when no hand is detected
            image_frame = create_image_frame(image1, image2, image3)
            isplay=False

        # Resize the video frame to match the image frame width
        image_frame_height, image_frame_width = image_frame.shape[:2]
        video_frame_width = image_frame_width
        video_frame_height = int(video_frame_width * frame.shape[0] / frame.shape[1])
        resized_frame = cv2.resize(frame, (video_frame_width, video_frame_height))

        # Stack video frame and image frame vertically
        combined_frame = np.vstack((resized_frame, image_frame))

        cv2.imshow("Finger Counter with Images", combined_frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
