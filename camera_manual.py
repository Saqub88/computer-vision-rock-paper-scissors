import numpy as np
import cv2
import keras
from keras.models import load_model

def camera_feed():
    keras.utils.disable_interactive_logging()
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224,224,), interpolation = cv2.INTER_AREA)
        cv2.imshow("Frame", frame)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0)

        ch = cv2.waitKey(1)

        if ch & 0xFF == ord('a'):
            data[0] = normalized_image
            prediction = model.predict(data)
            plays = ['Rock', 'Scissors', 'Paper', 'Nothing']
            RPS = (max(zip(prediction[0], plays))[1])
            print(RPS)
            verify = input(f"Enter 'y' if {RPS} is correct. Enter any other key if incorrect then press 'a' to retry")
            if verify.lower() == 'y':
                cap.release()
                cv2.destroyAllWindows()
                return RPS
        elif ch & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break