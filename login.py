import os
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def main():
    email = os.environ.get('EMAIL')
    passwd = os.environ.get('PASSWD')
    print(f"\n------正在处理------")

    # 配置 Chrome 选项
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1000,720")

    # 使用系统已安装的 ChromeDriver
    service = Service('/usr/local/share/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    try:
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

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
