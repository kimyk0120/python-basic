import pyautogui

pyautogui.click(315, 62)

x, y = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(x/2, y/2)

x, y = pyautogui.locateCenterOnScreen('+.png')
pyautogui.click(x/2, y/2)

x, y = pyautogui.locateCenterOnScreen('3.png')
pyautogui.click(x/2, y/2)
pyautogui.press('enter')