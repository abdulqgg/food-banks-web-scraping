from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/maps/d/u/0/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=50.80559354911368%2C-1.470568783234869&z=7'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links =  soup.find_all('a')

script_tag = soup.find('script', text=lambda x: x and '_pageData' in x)

# Extract the variable value from the tag
variable_value = script_tag.text.split('=')[1].strip().rstrip(';')

print(variable_value.type())

# example: print the text of all links on the page
for link in links:
    print(link.text)

# example: write links to a text file
with open('links.txt', 'w') as f:
    f.write(variable_value)

