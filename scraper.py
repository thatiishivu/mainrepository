import requests
from bs4 import BeautifulSoup
print('i love racchy')
response_out = requests.get('https://www.youtube.com/watch?v=FcW-AXsirBE')
print('connection status:',response_out.status_code)
with open('trending.html', 'w') as f:
  f.write(response_out.text)

doc = BeautifulSoup(response_out.text,'html.parser')

print('title of the document',doc.title.text)
print('racchu loves me')