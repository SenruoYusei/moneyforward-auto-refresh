import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


def main():
    load_dotenv()
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    # Define browser
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    print('start login')
    # Jump to email sing-in page
    url = 'https://moneyforward.com/sign_in'
    browser.get(url)
    sleep(1)

    # Enter email
    elem_loginMethod = browser.find_element(
        by=By.XPATH,
        value='/html/body/main/div/div/div[2]/div/section/div/form/div/div/input',
    )
    elem_loginMethod.send_keys(EMAIL)
    sleep(1)

    # Click Sign in
    elem_sign_in1 = browser.find_element(
        by=By.XPATH,
        value='/html/body/main/div/div/div[2]/div/section/div/form/div/button',
    )
    elem_sign_in1.click()
    sleep(1)

    # Enter password
    elem_password = browser.find_element(
        by=By.XPATH,
        value='/html/body/main/div/div/div[2]/div/section/div/form/div/div[2]/input',
    )
    elem_password.send_keys(PASSWORD)
    sleep(1)

    # Click login
    elem_sign_in2 = browser.find_element(
        by=By.XPATH,
        value='/html/body/main/div/div/div[2]/div/section/div/form/div/button',
    )
    elem_sign_in2.click()
    sleep(1)

    # get number of total asset
    elem_total_asset = browser.find_element(
        by=By.XPATH,
        value='/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/section[1]/section/div[1]',
    )
    total_asset = elem_total_asset.text
    print(f'Your total asset is {total_asset}')

    # Click "一括更新"
    elem_update = browser.find_element(
        by=By.XPATH,
        value='/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/section[3]/div/div[2]/a',
    )
    elem_update.click()
    sleep(1)


if __name__ == '__main__':
    main()
