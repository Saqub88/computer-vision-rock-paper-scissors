import numpy as np
import time
import cv2
import keras
from keras.models import load_model

def camera_feed():
    keras.utils.disable_interactive_logging()
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    cv2.namedWindow("Frame")
    start = time.time()
    
    while True:
        colour = (0,0,255)
        text_font = cv2.FONT_HERSHEY_SIMPLEX
        blah = "blah blah"
        line_width = 2
        point = (100,100)
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224,224), interpolation = cv2.INTER_AREA)
        cv2.imshow("Frame", frame)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0)
        current_time = str(round((4 - (time.time() - start)), 0))
        display_text = current_time
        cv2.putText(frame, blah, point, text_font, 1, colour, line_width, cv2.LINE_AA)
        if float(display_text) < 0:
             data[0] = normalized_image
             prediction = model.predict(data)
             plays = ['Rock', 'Scissors', 'Paper', 'Nothing']
             RPS = (max(zip(prediction[0], plays))[1])
             print(RPS)
             cap.release()
             cv2.destroyAllWindows()
             return RPS
        
        ch = cv2.waitKey(1)
        if ch & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

camera_feed()