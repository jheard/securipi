import cv2 as cv
import time
import os

IMG_DIR = "img/"
IMG_DELAY_SEC = 5
MINS_TO_RETAIN = 10
IMG_COUNT = (60 // IMG_DELAY_SEC) * MINS_TO_RETAIN

cap = cv.VideoCapture(0)
tries = 0
while not cap.isOpened() and tries < 20:
    tries += 1
    os.sleep(0.5)
if tries == 20:
    print("Failed to open camera")

try:
    os.listdir(IMG_DIR)
except FileNotFoundError:
    os.mkdir(IMG_DIR)

try:
    while True:
        time_stamp = int(time.time())
        filename = f"{IMG_DIR}{time_stamp}.jpg"
        ret, frame = cap.read()
        if not ret:
            exit()
        cv.imwrite(filename,frame)
        print(f"[-] Saved {time_stamp}")
        img_list = sorted(os.listdir(IMG_DIR))
        if len(img_list) > IMG_COUNT:
            os.remove(f"{IMG_DIR}{img_list[0]}")
            print(f"[!] Removed {img_list[0]}")
        time.sleep(IMG_DELAY_SEC)
except:
    cap.release()

