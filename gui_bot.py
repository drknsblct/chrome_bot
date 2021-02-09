import time
import pyautogui

num = int(input('Number of open tabs: '))

# while True:


# makes input lowercase and strips whitespace
# answer = input('Are there videos in tabs? [y/n] ').lower().strip()
# if answer[0] == 'y':
#     sleep_timer = 2.5
#     break
# elif answer[0] == 'n':
#     sleep_timer = 1.5
#     break
# else:
#     continue


def gui_bot(num):
    count = 0
    pyautogui.moveTo(1289, 768)  # position to move
    pyautogui.click()
    for i in range(num):
        pyautogui.hotkey('command', 's')
        # time.sleep(sleep_timer)
        time.sleep(2.5)

        pyautogui.hotkey('enter')
        pyautogui.hotkey('command', 'w')
        time.sleep(0.5)
        count += 1
    print(f'Total files downloaded: {count}')


if __name__ == '__main__':
    gui_bot(num)
