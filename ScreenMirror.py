import numpy as np
from PIL import ImageGrab
import cv2

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    return processed_img

while(True):
    printscreen_pil = np.array(ImageGrab.grab())
    new_screen = process_img(printscreen_pil)
    cv2.imshow('Window',new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
