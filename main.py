from bs4 import BeautifulSoup
import requests

url = 'https://www.foodaidnetwork.org.uk/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links =  soup.find_all('a')

print(soup)

# example: print the text of all links on the page
for link in links:
    print(link.text)

# example: write links to a text file
with open('links.txt', 'w') as f:
    for link in links:
        f.write(link['href'] + '\n')
