import cv2

# 1. Connect to your laptop's default webcam (0 is usually the built-in camera)
cap = cv2.VideoCapture(0)

print("Press 'q' on your keyboard to close the window!")

while True:
    # 2. Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break

    # 3. Display the video feed in a window named 'Robot Vision'
    cv2.imshow('Robot Vision', frame)

    # 4. Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Clean up and close everything down when done
cap.release()
cv2.destroyAllWindows()