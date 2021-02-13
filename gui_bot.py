import pyautogui


def photos_and_videos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # position to move
    pyautogui.click()

    for i in range(num):
        pyautogui.sleep(1)
        pyautogui.hotkey('command', 's')
        pyautogui.sleep(1.5)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.5)
        count += 1

    print(f'Total files downloaded: {count}')


def photos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # activates browser window
    pyautogui.click()

    for i in range(num):
        pyautogui.moveTo(1070, 1030)
        pyautogui.click()
        pyautogui.sleep(1)
        pyautogui.hotkey('command', 's')
        pyautogui.sleep(2) #1.5
        pyautogui.hotkey('enter')
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.1)
        pyautogui.hotkey('command', 'w')
        count += 1

    print(f'Total files downloaded: {count}')


if __name__ == '__main__':
    num = int(input('Number of open tabs: '))

    while True:
        answer = int(input('Photos[1] or Photos/Videos[2]? '))
        if answer == 1:
            photos(num)
            break
        elif answer == 2:
            photos_and_videos(num)
            break
        else:
            continue
