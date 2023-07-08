import os
from dotenv import load_dotenv
import pyautogui
import string
import time
import random

load_dotenv('.env')

# Image path
path = os.getenv('IMAGE_PATH')

def find_on_screen():
    #Locate the image on the screen and press 'enter'
    while not pyautogui.locateOnScreen(path, confidence=0.7):
        pass
    pyautogui.press('enter')


def find_on_screen_rename():
    #Locate the image on the screen, write a random string and press 'enter'
    random_text = ''.join(random.choices(f"{string.ascii_letters}{string.digits}", k=4))
    while not pyautogui.locateOnScreen(path, confidence=0.7):
        pass
    pyautogui.write(random_text)
    pyautogui.press('enter')


def photos_and_videos(num):
    #Download photos and videos
    pyautogui.moveTo(60, 60)
    pyautogui.click()

    for _ in range(num):
        pyautogui.hotkey('command', 's')
        find_on_screen()
        pyautogui.hotkey('command', 'w')


def rename_photos_and_videos(num):
    #Download and rename photos and videos
    pyautogui.moveTo(60, 60)
    pyautogui.click()

    for _ in range(num):
        pyautogui.hotkey('command', 's')
        find_on_screen_rename()
        pyautogui.hotkey('command', 'w')


if __name__ == '__main__':
    while True:
        try:
            num = int(input('\nNumber of tabs: '))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    actions = {1: photos_and_videos, 2: rename_photos_and_videos}

    while True:
        try:
            answer = int(input('Media [1] | Rename Media [2]: '))
            if answer in actions:
                start = time.time()
                actions[answer](num)
                print(
                    f'\nTime elapsed: {time.strftime("%M:%S", time.gmtime(time.time() - start))}\n')
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
