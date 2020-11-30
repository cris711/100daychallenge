import urllib.request
from bs4 import BeautifulSoup
inp='https://'
inp2 = input("Please enter a URL: ")
inp=inp+inp2
webUrl = urllib.request.urlopen(inp)

print("result code: " +str(webUrl.getcode()))

data = webUrl.read()
test = BeautifulSoup(data, 'html.parser')
print("Title of Website")
print(test.find("title"))
print(test.find("p"))

print(data)

