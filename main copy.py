from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Open chrome 
driver = webdriver.Chrome()

# Destinated website
driver.get("https://www.google.com/maps/d/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=51.89185325888764%2C1.659932842043248&z=8")

# Wait for page to load
driver.implicitly_wait(10)

# Finds and opens dropdown
actions = ActionChains(driver)
dropdown = driver.find_element(By.XPATH, '//*[@id="legendPanel"]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div[2]/div/div')
actions.move_to_element(dropdown).click().perform()

# Clicks on foodbank and goes back
def foodbank_back(index):
    foodbank = driver.find_element(By.XPATH, '//*[@id="legendPanel"]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div[3]/div[2]/div['+str(index)+']')
    foodbank.click()
    time.sleep(2)
    back = driver.find_element(By.XPATH, '//*[@id="featurecardPanel"]/div/div/div[3]/div[1]/div/span/span/span')
    actions.move_to_element(back).click().perform()
    time.sleep(2)

foodbank_back(1)
foodbank_back(6)

# Close the browser window
driver.quit()
