import cv2
import pytesseract
import pyautogui
import time

f = open("config.cfg", "r")
PATH = f.readline().strip()
t = float(f.readline().strip())
pause = int(f.readline().strip())
f.close()

start = time.time()
time.sleep(3)
pytesseract.pytesseract.tesseract_cmd = PATHe

screenshot = pyautogui.screenshot(region=(450, 250, 980, 600))
screenshot.save("test.png")

img = cv2.imread("test.png")
result = pytesseract.image_to_string(img)
print(result)
for c in result:
    if c == "\n":
        c = " "
    pyautogui.typewrite(c, t)

# while (time.time() - start) < pause:
#     screenshot = pyautogui.screenshot(region=(450, 280, 980, 70))
#     screenshot.save("test1.png")
#     img = cv2.imread("test1.png")
#     result = pytesseract.image_to_string(img)
#     print(result)
#     for c in result:
#         if c == "\n":
#             c = " "
#         pyautogui.typewrite(c, t)
