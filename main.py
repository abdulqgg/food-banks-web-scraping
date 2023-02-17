from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/maps/d/u/0/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=50.80559354911368%2C-1.470568783234869&z=7'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('div', class_='HzV7m-pbTTYe-SmKAyb-haAclf'))


# example: write links to a text file
# with open('links.txt', 'w') as f:
#     f.write(variable_value)

#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure the Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# Launch a Chrome browser using the ChromeDriver executable
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# Navigate to the URL of the custom Google Map
driver.get('https://www.google.com/maps/d/u/0/viewer?mid=YOUR_MAP_ID&ll=YOUR_LATITUDE,YOUR_LONGITUDE&z=YOUR_ZOOM_LEVEL')

# Wait for the map to load
driver.implicitly_wait(10)

# Click on each marker to load its info window
markers = driver.find_elements_by_class_name('suEOdc')

for marker in markers:
    marker.click()

# Extract the HTML of the map
html = driver.page_source

# Parse the HTML with BeautifulSoup to extract the names and addresses of the markers
soup = BeautifulSoup(html, 'html.parser')
marker_infos = soup.find_all('div', class_='section-info-line')

for info in marker_infos:
    name = info.find('h3', class_='section-info-title').text
    address = info.find('div', class_='section-info-address').text
    print(name, address)

# Close the browser
driver.quit()
