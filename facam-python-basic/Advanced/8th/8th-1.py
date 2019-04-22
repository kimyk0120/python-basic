import pyautogui
import time

pyautogui.moveTo(631, 123)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(544, 124)
pyautogui.click()
time.sleep(0.5)
# pyautogui.moveRel(100, 200)
pyautogui.click(585, 523)
time.sleep(0.5)
pyautogui.press('shift')
# pyautogui.typewrite("# typewrite test") # 키보드를 누르는것 , 한글입력은 해당 키를 입력해야함
pyautogui.press('enter')

# typewrite test
# 쇼ㅔㄷㅈ걋ㄷ ㅅㄷㄴㅅ <- typewrite test
# typewrite test

pyautogui.screenshot("result.png")
