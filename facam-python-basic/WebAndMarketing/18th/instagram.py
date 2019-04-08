'''
    인스타 로그인, 해시태그검색, 좋아요
'''

import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

d = webdriver.Chrome('./chromedriver')

try:
    # 인스타그램으로 이동한다
    d.get('https://www.instagram.com')

    f = open("./user.properties", 'r')
    ID = f.readline().strip()
    PW = f.readline().strip()

    # # 화면이 다 준비되지 않았을 때를 대비하여 1초간 대기
    time.sleep(1)
    # # 페이스북 로그인인 경우 페이스북 로그인 버튼을 찾아 클릭한다
    # elem = d.find_element_by_class_name('_0mzm-')
    # elem.click()
    #
    # # 주석처리된 이 코드는 인스타그램 로그인인 경우 클릭
    # # '로그인'이라는 문자열이 포함된 링크(a태그)를 찾는다
    elem = d.find_element_by_link_text('로그인')
    elem.click()

    # # 로그인 페이지가 나올때까지 대기한다
    time.sleep(2)

    # # 주석처리된 코드는 인스타그램의 아이디 영역
    # # 주석처리되지 않은 코드는 페이스북 로그인
    elem = d.find_element_by_name('username')
    # elem = d.find_element_by_name('email')
    elem.send_keys(ID)

    # # 주석처리된 코드는 인스타그램의 비밀번호 영역
    # # 주석처리되지 않은 코드는 페이스북 로그인
    elem = d.find_element_by_name('password')
    # elem = d.find_element_by_name('pass')
    elem.send_keys(PW)
    elem.send_keys(Keys.RETURN)

    time.sleep(2)

    try:
        # 알림설정 창이 뜨는 경우 이를 닫는다.
        # 안뜨는 경우도 있기 때문에 try~except 로 묶어서 에러를 막는다
        elem = d.find_element_by_class_name('HoLwm')
        elem.click()
    except Exception as e:
        print(e)

    # 해시태그 검색칸을 찾는다
    # div 태그는 키를 받을 수 없는 태그다 (몰라도 된다!)
    # ActionChains 를 사용하는데, 마우스를 테스트할 수 있다
    # 가상의 마우스라고 생각하면 됨
    elem = d.find_element_by_class_name('eyXLr')
    ac = ActionChains(d)
    # 위에서 찾은 태그위치로 마우스를 이동한다
    ac.move_to_element(elem)

    time.sleep(0.5)

    # 클릭한다
    ac.click()
    # 키를 누른다
    ac.send_keys('#pycoders')
    # 위 등록한 동작들을 실행한다
    ac.perform()

    time.sleep(2)

    # ActionChains 는 다시사용할때 앞에서 등록한 액션을 초기화해줘야한다
    ac.reset_actions()
    # 아래로 살짝 움직인다.(50px)
    ac.move_by_offset(0, 50)
    ac.click()
    ac.perform() # all stored actions.

    time.sleep(5)

    # 게시글을 전부 가져온다
    elem = d.find_element_by_class_name('EZdmt')
    posts = elem.find_elements_by_class_name('v1Nh3')
    ac = ActionChains(d)
    for idx, post in enumerate(posts):
        print(idx)
        # 반복문을 돌면서 액션을 초기화하고 각 게시글을 클릭한다
        ac.reset_actions()
        ac.move_to_element(post)
        ac.click()
        ac.perform()

        time.sleep(2)

        # 좋아요 클릭
        try:
            ac.reset_actions()
            elem = d.find_element_by_class_name('fr66n')
            ac.move_to_element(elem)
            ac.click()
            ac.perform()
        except:
            print("already clicked")

        time.sleep(1)

        # 창닫기
        ac.reset_actions()
        ac.send_keys(Keys.ESCAPE)
        ac.perform()

        time.sleep(1)

    # input()
except Exception as e:
    print(e)
finally:
    d.close()
    d.quit()
