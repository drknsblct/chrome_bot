import string
import time
import pyautogui
import random

path = '/Users/blackout/Projects/Chrome_Bot/image/savePhoto.png'


def findOnScreen():
    if pyautogui.locateOnScreen(path, region=(2714, 430, 154, 46),
                                confidence=0.9):

        pyautogui.press('enter')
    else:
        findOnScreen()


# locates image on screen and inputs text on prompt
def findOnScreenDiscord():
    random_text = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=4))
    if pyautogui.locateOnScreen(path, region=(2714, 430, 154, 46),
                                confidence=0.9):
        pyautogui.write(random_text)
        pyautogui.press('enter')
    else:
        findOnScreenDiscord()


# downloads photos and videos
def photos_and_videos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # position to move
    pyautogui.click()

    for _ in range(num):
        pyautogui.hotkey('command', 's')
        findOnScreen()
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.5)
        count += 1


# downloads photos and videos and changes their name
def photos_and_videos_discord(num):
    count = 0
    pyautogui.moveTo(60, 60)  # position to move
    pyautogui.click()

    for _ in range(num):
        pyautogui.hotkey('command', 's')
        findOnScreenDiscord()
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.5)
        count += 1


# downloads only photos
def photos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # activates browser window
    pyautogui.click()

    for _ in range(num):
        pyautogui.moveTo(1063, 999)
        pyautogui.keyDown('option')
        pyautogui.click()
        pyautogui.keyUp('option')
        pyautogui.sleep(0.1)
        pyautogui.hotkey('command', 'w')
        count += 1


if __name__ == '__main__':
    print()
    while True:
        try:
            num = int(input('Number of tabs: '))
            break
        except Exception:
            continue

    while True:
        try:
            answer = int(input('Photos[1] | Photos/Videos[2] | Discord[3]: '))
        except Exception:
            continue

        if answer == 1:
            start = time.time()
            photos(num)
            break
        elif answer == 2:
            start = time.time()
            photos_and_videos(num)
            break
        elif answer == 3:
            start = time.time()
            photos_and_videos_discord(num)
            break
        else:
            continue

    print(f'\nTime elapsed: {time.strftime("%M:%S", time.gmtime(time.time() - start))}\n')
