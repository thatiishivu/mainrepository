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


urltohit_onreplit = 'https://app.flexera.com/suite'
driver = get_driver()
driver.get(urltohit_onreplit)
delay = 3  # seconds


def wait_untilelemwntLoads(driver, element, delay):
    print('mehtod is called')
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, element)))
        print(element + ' On Page is ready!')
    except TimeoutException:
        print('Loading took too much time!')


wait_untilelemwntLoads(driver, 'okta-signin-username', 3)

element_UN = driver.find_element(By.ID, 'okta-signin-username')
element_PWD = driver.find_element(By.ID, 'okta-signin-password')
element_UN.send_keys('fnmpadministrator@uat.thc.test')

element_PWD.send_keys('J4x%mLk^v8lU13')
element_LogIn = driver.find_element(By.ID, 'okta-signin-submit')
element_LogIn.click()

wait_untilelemwntLoads(driver, 'accept-cookies-button', 30)
element_acceptcookies = driver.find_element(By.ID,'accept-cookies-button')
element_acceptcookies.click()

driver.get('https://app.flexera.com/orgs/28062/slo/Suite/Licenses/List/All')

wait_untilelemwntLoads(driver, 'header-profile-button', 30)
element_headerprofile = driver.find_element(By.ID,'header-profile-button')
# element_headerprofile.click()
driver.execute_script("arguments[0].click();", element_headerprofile)

element_logoutbutton = driver.find_element(By.XPATH,"//button[text()='Log out']")
driver.execute_script("arguments[0].click();", element_logoutbutton)

wait_untilelemwntLoads(driver, 'okta-signin-username', 90)
# wait_untilelemwntLoads(driver, 'fnms-iframe', 30)
# driver.switch_to.frame('fnms-iframe')
