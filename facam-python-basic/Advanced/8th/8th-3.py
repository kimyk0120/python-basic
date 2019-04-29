"""
    카카오톡
"""

import subprocess # 프로세스 관리하는 패키지
import pyautogui
import time

# mac
kakao = subprocess.Popen(['open', '-a', 'kakaotalk'])
# win
# kakao = subprocess.Popen(['c:\\Program Files\\Kakao\\Kakaotalk.exe'])


#  로그인
# import myid
# myId = myid.ID
# myPw = myid.PW
# pyautogui.typewrite(myId)
# pyautogui.press("tab")
# pyautogui.typewrite(myPw)


time.sleep(1)

# x, y = pyautogui.locateCenterOnScreen('profile.png') # 맥 사용자는 x, y 에 2를 나눠야함
# pyautogui.moveTo(x, y)
pyautogui.doubleClick(1600, 303)

time.sleep(0.5)
pyautogui.doubleClick(1600, 274)
pyautogui.typewrite("Test Message")
pyautogui.press("enter")








