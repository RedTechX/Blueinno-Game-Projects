import pytesseract
import pyautogui as gui
from PIL import ImageGrab as shot

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
gui.PAUSE = 0    

# gui.displayMousePosition()

left = 1479 #X
right = 2838 #X
top = 735 #Y
botm = 814 #Y


gui.click(left, top - 20)

FILE_NAME = 'words.png'
screenshot = shot.grab(bbox = (left,top,right,botm))
screenshot.save(FILE_NAME)

height = botm - top + 15
top += height
botm += height

while True:
    text = pytesseract.image_to_string(FILE_NAME, lang = 'eng')
    # print(text)
    gui.typewrite(text, interval=0)
    gui.typewrite(' ')
    
    
    screenshot = shot.grab(bbox = (left,top,right,botm))
    screenshot.save(FILE_NAME)