from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
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
    time.sleep(0.3)
    # call to extract data
    for i in range(1,6):
        get_info(i)
    back = driver.find_element(By.XPATH, '//*[@id="featurecardPanel"]/div/div/div[3]/div[1]/div/span/span/span')
    actions.move_to_element(back).click().perform()
    time.sleep(0.3)

# Extracting foodbank data
def get_info(index_info):
    # try to retrieve data
    try:
        # extracting head and data
        # e.g info_head = Organisation and info_data = Foodbank-name
        info_head = driver.find_element(By.XPATH, '//*[@id="featurecardPanel"]/div/div/div[4]/div[1]/div['+str(index_info)+']/div[1]')
        info_data = driver.find_element(By.XPATH, '//*[@id="featurecardPanel"]/div/div/div[4]/div[1]/div['+str(index_info)+']/div[2]')
    except NoSuchElementException:
        # catch if no data
        pass
    else:
        # if data save it to file
        with open('foodbank_data_1.txt', 'a') as f:
            f.write(info_head.text + ':' + info_data.text + '\n')


# Get data for all the foodbanks
for i in range(1,759):
     foodbank_back(i)



# Close the browser window
driver.quit()
