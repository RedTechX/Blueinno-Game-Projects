import pyautogui as gui
from PIL import ImageGrab
import threading

stop_event = threading.Event()

gui.pause = 0.07

def main_task():
    x = 2500
    y = 680
    
    try:
        while True:
            gui.click(x, y)
    except Exception as e:
        stop_event.set()

def perk_task():
    perks = [
        'CCImages/power.png',
        'CCImages/ore_quality.png',
        'CCImages/price.png',
    ]
    
    w = 507
    h = 125
    orange = (252, 126, 0)

    scr_dis = 0
    scr_spd = -10
    while True:
        if stop_event.is_set():
            break
        
        screenshot = ImageGrab.grab()
        pixels = screenshot.load()
        
        for img in perks:
            try:
                # Box(left=1579, top=706, width=116, height=134)
                box = gui.locateOnScreen(img, confidence=0.85)
                print(f'found on: {box}')
                pileft = box.left                
                pitop = box.top
                x = pileft + 394
                y = pitop + 100
                
                while pixels[x,y] == orange:
                   print('is orange!')
                   gui.click(x, y)
                   screenshot = ImageGrab.grab()
                   pixels = screenshot.load()
                
            except gui.ImageNotFoundException:
                print(f'image ({img}) not found')
                gui.moveTo(1679, 706)
                gui.scroll(scr_spd)
                scr_dis += scr_spd
                
                if scr_dis >= 50 or scr_dis <= -50:
                    scr_spd *= -1
                
            except Exception as e:
                print(f'e: {e}')


t1 = threading.Thread(target=main_task)
t2 = threading.Thread(target=perk_task)


try:
    t1.start()
    t2.start()
except Exception as e:
    stop_event.set()
    t1.join()
    t2.join()

#gui.displayMousePosition()

#  1930

#733
#901
#1066

px = 1940
py_start = 735
py_end = 1068



    
    
    
    