import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

accounts = int(len(sys.argv[1:])/2)
for i in range(accounts):
    email = sys.argv[1 + i]
    passwd = sys.argv[1 + i + accounts]

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.com/1/")

    sleep(20)

    # 2. 输入邮箱
    screen = driver.find_element(By.ID, 'layaCanvas')
    ActionChains(driver) \
        .move_to_element_with_offset(screen, 250, -100) \
        .click() \
        .perform()

    email_input = driver.find_element(By.NAME, 'input')
    email_input.clear()
    email_input.send_keys(email)
    print('账号输入成功')
    sleep(2)

    # 3. 输入密码
    ActionChains(driver) \
        .move_to_element_with_offset(screen, 250, -50) \
        .click() \
        .perform()

    password_input = driver.find_element(By.NAME, 'input_password')
    password_input.clear()
    password_input.send_keys(passwd)
    print('密码输入成功')
    sleep(2)

    # 4. 登录
    ActionChains(driver) \
        .move_to_element_with_offset(screen, 250, 50) \
        .click() \
        .perform()
    sleep(20)
    print('登录成功')

    driver.quit()


