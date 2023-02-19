from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Start a new Chrome browser window
driver = webdriver.Chrome()

# Navigate to the webpage containing the element you want to extract
driver.get("https://www.google.com/maps/d/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=51.89185325888764%2C1.659932842043248&z=8")

# Wait for the page to load and display the element you want to extract
# (you may need to adjust the wait time depending on the page load speed)
driver.implicitly_wait(10)

# Css selector
csselector = "#legendPanel > div > div > div.i4ewOd-PBWx0c-bN97Pc-haAclf > div > div > div.i4ewOd-pbTTYe-haAclf > div > div > div.HzV7m-pbTTYe-bN97Pc > div.HzV7m-pbTTYe-JNdkSc > div.HzV7m-pbTTYe-JNdkSc-PntVL"
dropdowncss = "#legendPanel > div > div > div.i4ewOd-PBWx0c-bN97Pc-haAclf > div > div > div.i4ewOd-pbTTYe-haAclf > div > div > div.HzV7m-pbTTYe-bN97Pc.HzV7m-pbTTYe-bN97Pc-qAWA2 > div.HzV7m-pbTTYe-KoToPc-ornU0b-haAclf > div > div"

# Find the element using the CSS selector you provided
#element = driver.find_element(By.CSS_SELECTOR, csselector)

#dropdown element and click
dropdown = driver.find_element(By.CSS_SELECTOR, dropdowncss)
ActionChains(driver).move_to_element(dropdown).click().perform()

desired_element = driver.find_element(By.CSS_SELECTOR, csselector)

# Extract the text content of the element
element_text = desired_element.text

# Print the extracted text
print(element_text)

# Close the browser window
driver.quit()
