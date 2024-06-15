import pyautogui as gui
import multiprocessing as mp

# gui.displayMousePosition()

gui.PAUSE = 0.000005

main_btn_pos = (2016, 690)
upgd_btn_pos = [
    (2763, 567),
    (2763, 671),
    (2763, 770),
    (2763, 870),
    (2763, 972),
]

def click_main():
    while True:
        gui.click(main_btn_pos)


def click_upgd():
    while True:
        for x, y in upgd_btn_pos:
            gui.click(x, y)
        
if __name__ == '__main__':
    main_process = mp.Process(target = click_main)
    upgd_process = mp.Process(target = click_upgd)
    main_process.start()
    upgd_process.start()