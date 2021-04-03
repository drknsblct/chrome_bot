import string
import time
import pyautogui
import random


# locates image on screen
def findOnScreen():
    if pyautogui.locateOnScreen('/Users/blackout/Scraper/Gui_Bot/image/savePhoto.png', region=(2716, 562, 148, 34), confidence=0.9):
        pyautogui.press('enter')
    else:
        findOnScreen()


# locates image on screen and inputs text on prompt
def findOnScreenDiscord():
    random_text = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=4))
    if pyautogui.locateOnScreen('/Users/blackout/Scraper/Gui_Bot/image/savePhoto.png', region=(2716, 562, 148, 34), confidence=0.9):
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
        pyautogui.sleep(0.5)  # 0.5
        count += 1

    print(f'\nTotal files downloaded: {count}')


# downloads photos and videos and changes their name
def photos_and_videos_discord(num):
    count = 0
    pyautogui.moveTo(60, 60)  # position to move
    pyautogui.click()

    for _ in range(num):
        pyautogui.hotkey('command', 's')
        findOnScreenDiscord()
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.5)  # 0.5
        count += 1

    print(f'\nTotal files downloaded: {count}')


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
        pyautogui.sleep(0.1)  # 0.1
        pyautogui.hotkey('command', 'w')
        count += 1

    print(f'\nTotal files downloaded: {count}')


if __name__ == '__main__':
    num = int(input('Number of open tabs: '))

    while True:
        answer = int(input('Photos[1] | Photos/Videos[2] | Discord[3]: '))
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

    print(f'Time elapsed: {time.strftime("%M:%S", time.gmtime(time.time() - start))}')
