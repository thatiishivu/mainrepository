#https://www.youtube.com/watch?v=FcW-AXsirBE
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

print('i love racchy')
response_out = requests.get('https://www.youtube.com/watch?v=FcW-AXsirBE')
print('connection status:', response_out.status_code)
with open('trending.html', 'w') as f:
    f.write(response_out.text)

doc = BeautifulSoup(response_out.text, 'html.parser')

print('title of the document', doc.title.text)
print('racchu loves me')


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


urltohit_onreplit = 'https://sit.app.flexeratest.com/?fnms-host=https://SYS16-SERVER2.fnms.flexdev.com&?fnms-cookie-refresh=https://SYS16-SERVER2.fnms.flexdev.com/Suite/Login/CookieRefresher'
driver = get_driver()
driver.get(urltohit_onreplit)
delay = 3  # seconds


def wait_untilelemwntLoads(driver, element, delay):
    print('mehtod is called')
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, element)))
        print(element + 'On Page is ready!')
    except TimeoutException:
        print('Loading took too much time!')


wait_untilelemwntLoads(driver, 'okta-signin-username', 3)

element_UN = driver.find_element(By.ID, 'okta-signin-username')
element_PWD = driver.find_element(By.ID, 'okta-signin-password')
element_UN.send_keys('fnmpautouser0@thc.test')

element_PWD.send_keys('G0dz111a@2050$$')
element_LogIn = driver.find_element(By.ID, 'okta-signin-submit')
element_LogIn.click()

wait_untilelemwntLoads(driver, 'accept-cookies-button', 30)
driver.get('https://app.flexeratest.com/orgs/40079/slo/Suite/MyPreferences')

wait_untilelemwntLoads(driver, 'fnms-iframe', 30)
driver.switch_to.frame('fnms-iframe')
print(driver.title)
