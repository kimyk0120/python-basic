import subprocess
import pyautogui
import time

kakao = subprocess.Popen(['open', '-a', 'KakaoTalk'])
time.sleep(1)

from myid import ID, PW

pyautogui.typewrite(ID)
pyautogui.press('tab')
pyautogui.typewrite(PW)
pyautogui.press('enter')

time.sleep(2)

x, y = pyautogui.locateCenterOnScreen('profile.png')
x = x/2 + 120
y = y/2

pyautogui.doubleClick(x, y)

pyautogui.typewrite('Test message')
pyautogui.press('enter')
