# 스크린샷을 이용한 화면의 위치 찾기

import pyautogui
import time

# result.png (스크린샷) 화면에서 미리보기후 선택할 위치를
# 박스드래그 cmd + c , cmd + n 으로 해방 위치의 이미지를 추출
# 이후 locateCenterOnScreen 함수를 이용하여 선택
x, y = pyautogui.locateCenterOnScreen("ref.png")
pyautogui.click(x, y)
