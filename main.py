import os
import cv2
import load
import keyboard
import recognize


temp_folder = r"\your\folder\path\here"
known_faces_folder = r"\your\folder\path\here"
temp_picture = r"\your\folder\path\here\picture.jpg"

# Open a connection to the camera (0 is the default camera)
camera_capture = cv2.VideoCapture(0)
camera_capture.set(cv2.CAP_PROP_FPS, 60)  # sets the frame rate

while True:
    # Capture each frame from the camera
    _, frame = camera_capture.read()

    # Display the frame in a preview window
    cv2.imshow("Press 'Tab' to capture temp or 'Shift+C' to capture a new Known Face", frame)

    # Check for tab key press
    if keyboard.is_pressed("tab"):  # temp capture
        # Temp image name
        image_name = "picture.jpg"

        # Specify the path where the image will be saved
        image_path = os.path.join(temp_folder, image_name)

        # Save the captured frame as an image
        cv2.imwrite(image_path, frame)

        print("loading...")

        known_faces, known_names = load.saved_known_faces(known_faces_folder)
        recognize.face(temp_picture, known_faces, known_names)

    # Check for shift+c key presses
    if keyboard.is_pressed("shift+c"):  # new known face capture
        # Allow the user to input a name for the image
        image_name = input("Enter a name: ") + ".jpg"

        # Specify the path where the image will be saved
        image_path = os.path.join(known_faces_folder, image_name)

        # Save the captured frame as an image
        cv2.imwrite(image_path, frame)

        print(f"'{image_name.split(".")[0]}' saved.")
        print("\n")

    # Check for 'Esc' key press to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close OpenCV windows
camera_capture.release()
cv2.destroyAllWindows()
