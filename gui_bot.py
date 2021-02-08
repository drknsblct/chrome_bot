import pyautogui
import time

num = int(input("How many open tabs? "))


def gui_bot(num):
    pyautogui.moveTo(1289, 768)  # position to move
    pyautogui.click()
    for i in range(num):
        pyautogui.hotkey('command', 's')

        time.sleep(2)

        pyautogui.hotkey('enter')
        pyautogui.hotkey('command', 'w')
        time.sleep(1)
    print('Done')


if __name__ == '__main__':
    gui_bot(num)
