import pyautogui
import time

num = int(input("Number of open tabs: "))


def gui_bot(num):
    count = 0
    pyautogui.moveTo(1289, 768)  # position to move
    pyautogui.click()
    for i in range(num):
        pyautogui.hotkey('command', 's')
        time.sleep(1.5)

        pyautogui.hotkey('enter')
        pyautogui.hotkey('command', 'w')
        time.sleep(0.5)
        count += 1
        print(f'Image: {count}')
    print('Done')


if __name__ == '__main__':
    gui_bot(num)
