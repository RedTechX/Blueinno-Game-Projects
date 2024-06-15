import pyautogui as gui
from PIL import ImageGrab as scrncptr
from time import sleep as delay

#gui.displayMousePosition()

gui.PAUSE = 0.0
gui.click(2069, 1445)

x_s = [1892, 2068, 2244, 2421]
y = 1220
cHeight = 240
HI = 200
BR = 220
LO = 100

def color(rgb) -> str:
    r, g, b = rgb
    # print(rgb)
    # print([r, g, b])
    
    if r > HI and g > HI and b > HI:
        return 'W'
    
    if r > HI and g < LO and b < LO:
        return 'r'
    
    if r < LO and g > HI and b < LO:
        return 'g'

    if r < LO and g < LO and b > HI:
        return 'b'
    
    if r < LO and g < LO and b < LO:
        return 'B'

    return '?'

def get_key(cells: list) -> str:
    key = None
    
    colorStr = ''.join(cells)
    
    if colorStr == 'grrr':
        return 'h'
    if colorStr == 'rgrr':
        return 'j'
    if colorStr == 'rrgr':
        return 'k'
    if colorStr == 'rrrg':
        return 'l'
    
    return key


def getCells(y: int) -> str:
    cells = [color(pixels[x, y]) for x in x_s]
    u_cells = [color(pixels[x, y - 8]) for x in x_s]
    d_cells = [color(pixels[x, y + 8]) for x in x_s]
    
    if not (cells == u_cells and cells == d_cells):
        return ['?', '?', '?', '?']

    return cells

while True:
    screenshot = scrncptr.grab()
    pixels = screenshot.load()
    
    pr = pixels[2257, 815]

    if color(pr) == 'W':
        delay(2)
        gui.click(2055, 1451)
    
    for i in range(3):
        y_center = y - i * cHeight
        cells = getCells(y_center)
        key = get_key(cells)
        if key:
            gui.press(key)
            
            # print([pixels[x, y_center] for x in x_s])
            # print([pixels[x, y_center-8] for x in x_s])
            # print([pixels[x, y_center+8] for x in x_s])
            
            # print(f'{i}: {cells}   {key}')
        
            if i == 2:
                delay(0.18)
        else:
            break
    # for i in range(3):
    #     y_center = y - i * cHeight
    #     cells = getCells(y_center+8)
        
    #     print(cells)
    #     for j in range(4):
    #         if(cells[j] == 'g'):
    #             gui.click(x_s[j], y_center)


    
        
        