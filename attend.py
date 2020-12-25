from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from userinfo import idtxt, pwd, url

framename = 'frame3'
idbox = 'input[name="dlfma"]'
passbox = 'input[name="dkagh"]'
loginbox = '#Table_01 > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > label'
logoutbox = 'body > div:nth-child(3) > table:nth-child(1) > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2) > label:nth-child(15)'
outbox = 'body > div:nth-child(3) > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(5) > tbody > tr > td > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td'



options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def login_logout(index) :
    driver.get(url)
    driver.switch_to.frame(driver.find_element_by_name(framename))

    driver.find_element_by_css_selector(idbox).send_keys(idtxt)
    driver.find_element_by_css_selector(passbox).send_keys(pwd)
    driver.find_element_by_css_selector(loginbox).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, logoutbox)
        )
    )

    if index == 1:
        tmpTime = driver.find_element_by_css_selector(outbox).text
        print(tmpTime)
        driver.close()

    if index == 0:
        driver.find_element_by_css_selector(logoutbox).click()

        WebDriverWait(driver, 3).until(
            EC.alert_is_present()
        )
        alert = driver.switch_to.alert

        alert_text = alert.text
        if alert_text != '' :
            print(alert_text, ' Success!')
        alert.accept()


for i in range(0, 2):
    login_logout(i)



