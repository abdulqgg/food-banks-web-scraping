from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Open chrome 
driver = webdriver.Chrome()

# Destinated website
driver.get("https://www.google.com/maps/d/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=51.89185325888764%2C1.659932842043248&z=8")

# Wait for page to load
driver.implicitly_wait(10)

# Css selectors
csselector = "#legendPanel > div > div > div.i4ewOd-PBWx0c-bN97Pc-haAclf > div > div > div.i4ewOd-pbTTYe-haAclf > div > div > div.HzV7m-pbTTYe-bN97Pc > div.HzV7m-pbTTYe-JNdkSc > div.HzV7m-pbTTYe-JNdkSc-PntVL"
dropdowncss = "#legendPanel > div > div > div.i4ewOd-PBWx0c-bN97Pc-haAclf > div > div > div.i4ewOd-pbTTYe-haAclf > div > div > div.HzV7m-pbTTYe-bN97Pc.HzV7m-pbTTYe-bN97Pc-qAWA2 > div.HzV7m-pbTTYe-KoToPc-ornU0b-haAclf > div > div"

# Dropdown element and click
dropdown = driver.find_element(By.CSS_SELECTOR, dropdowncss)
ActionChains(driver).move_to_element(dropdown).click().perform()

# Find the element 
desired_element = driver.find_element(By.CSS_SELECTOR, csselector)

element_text = desired_element.text

with open('foodbank_names.txt', 'w') as f:
    f.write(element_text + '\n')


# Close the browser window
driver.quit()
