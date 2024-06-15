import pyautogui as gui
from PIL import ImageGrab
import numpy as np

gui.PAUSE = 0
# gui.displayMousePosition()

left = 1820
top = 1161
right = 2203
bottom = 1228

imgz = ImageGrab.grab(
    bbox=(left, top, right, bottom)
)
imgz.save('clkarzmx.png')




keys = ['s','d','f','space','j','k','l']
div_width=(right-left) // len(keys) # 50 px

empty_divs = []
for i in range(len(keys)):
    start_x = i * div_width
    end_x = (i+1) * div_width

    div = imgz.crop((start_x, 0, end_x, imgz.height))
    div.save(f'div_{i}.png')

    gray_div = div.convert('L')
    gray_div.save(f'gray_div_{i}.png')

    px = np.array(gray_div)
    empty_divs.append(px)


print('You may start the game now!')
while True:
    latest_img = ImageGrab.grab(
        bbox=(left,top,right,bottom)
    )
    # latest_img.save('latest.png')
    
    latest_divs = []
    for i in range(len(keys)):
        start_x = i * div_width
        end_x = (i+1) * div_width

        div = latest_img.crop((start_x, 0, end_x, imgz.height))

        gray_div = div.convert('L')

        px = np.array(gray_div)
        latest_divs.append(px)
    
    for i in range(len(keys)):
        img1 = empty_divs[i]
        img2 = latest_divs[i]
        
        '''
        img1 = [3, 2, 1]
        img2 = [1, 2, 3]
        
        img3 = [2, 0, -2]
        img3 = [4, 0, 4]
        '''
        
        
        img3 = img1.astype('float') - img2.astype('float')
        img3 = img3 ** 2
        diff = np.sum(img3)
        diff /= float(img1.shape[0] * img1.shape[1])
        
        if diff >  2800:
            gui.keyDown(keys[i])
        else:
            gui.keyUp(keys[i])