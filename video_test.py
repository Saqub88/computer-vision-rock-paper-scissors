import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
start = time.time()
colour = (0,0,255)

text_font = cv2.FONT_HERSHEY_SIMPLEX
line_width = 2
point = (50,400)

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)

while True:
    ret, frame = cap.read()
    display_text = str(round((time.time() - start), 0))
    frame = cv2.resize(frame, (0,0), fx=1,fy=1)
    cv2.putText(frame, display_text, point, text_font, 1, colour, line_width, cv2.LINE_AA)
    cv2.imshow("Frame",frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()