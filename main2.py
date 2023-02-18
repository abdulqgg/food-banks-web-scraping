from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a new Chrome browser window
driver = webdriver.Chrome()

# Navigate to the webpage containing the element you want to extract
driver.get("https://www.google.com/maps/d/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=51.89185325888764%2C1.659932842043248&z=8")

# Wait for the page to load and display the element you want to extract
# (you may need to adjust the wait time depending on the page load speed)
driver.implicitly_wait(10)

# Find the element using the CSS selector you provided
element = driver.find_element(By.CSS_SELECTOR, "#legendPanel")

# Extract the text content of the element
element_text = element.text

# Print the extracted text
print(element_text)

# Close the browser window
driver.quit()
