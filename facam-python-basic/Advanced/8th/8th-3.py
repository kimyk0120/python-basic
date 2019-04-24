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







