import pyautogui as gui

gui.displayMousePosition()

while True:
    try:
        pos = gui.locateOnScreen('CCImages/ore_quality.png', confidence=0.85)
        print(f'mouse: {gui.position()}, found on: {pos}')
        pos = None
    except gui.ImageNotFoundException:
        print('image not found')
    except Exception as e:
        print(f'e: {e}')