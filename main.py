from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

# Configure the Chrome options to run in headless mode
chrome_options = Options()
#chrome_options.add_argument('--headless')

# Launch a Chrome browser using the ChromeDriver executable
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# Navigate to the URL of the custom Google Map
driver.get('https://www.google.com/maps/d/u/0/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=51.64010438452066%2C1.3356308175781262&z=9')

# Wait for the map to load
driver.implicitly_wait(10)

# Click on each marker to load its info window
search_box = driver.find_element_by_css_selector('#legendPanel > div > div > div.i4ewOd-PBWx0c-bN97Pc-haAclf > div > div > div.i4ewOd-pbTTYe-haAclf > div > div > div.HzV7m-pbTTYe-bN97Pc > div.HzV7m-pbTTYe-JNdkSc > div.HzV7m-pbTTYe-JNdkSc-PntVL')


# for marker in markers:
#     print(marker)
#     marker.click()

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
