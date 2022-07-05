#https://www.youtube.com/watch?v=FcW-AXsirBE
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('i love racchy')
response_out = requests.get('https://www.youtube.com/watch?v=FcW-AXsirBE')
print('connection status:',response_out.status_code)
with open('trending.html', 'w') as f:
  f.write(response_out.text)

doc = BeautifulSoup(response_out.text,'html.parser')

print('title of the document',doc.title.text)
print('racchu loves me')

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
urltohit_onreplit = 'https://www.youtube.com/watch?v=FcW-AXsirBE'
driver.get(urltohit_onreplit)

