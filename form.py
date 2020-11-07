from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

googleChromeOptions = webdriver.chrome.options.Options()
googleChromeOptions.headless = True
googleChromeOptions.add_argument('--window-size=1280,720')


web = webdriver.Chrome(executable_path="./chromedriver.exe",
options=googleChromeOptions)

#web = webdriver.Chrome(executable_path="./chromedriver.exe",
#options=googleChromeOptions)
web.get('https://www.eventsforce.net/standrews2/frontend/reg/thome.csp?pageID=661&eventID=3&traceRedir=2')

time.sleep(2)


redirectLink = web.find_element_by_xpath('//*[@id="div_664"]/div/h1/a')
redirectLink.click()

id = 200032337
firstName = "Rohan"
lastName = "Kumar"
mobNumber = 7978254787

time.sleep(2)

getId = web.find_element_by_xpath('/html/body/form/div[1]/div[3]/div/table[1]/tbody/tr[1]/td[2]/input')
getId.send_keys(id)

getFirstName = web.find_element_by_xpath('/html/body/form/div[1]/div[3]/div/table[1]/tbody/tr[3]/td[2]/input')
getFirstName.send_keys(firstName)

getLastName = web.find_element_by_xpath('/html/body/form/div[1]/div[3]/div/table[1]/tbody/tr[4]/td[2]/input')
getLastName.send_keys(lastName)

getMobNumber = web.find_element_by_xpath('/html/body/form/div[1]/div[3]/div/table[1]/tbody/tr[5]/td[2]/input')
getMobNumber.send_keys(mobNumber)

proceedButton = web.find_element_by_xpath('/html/body/form/div[1]/div[3]/div/table[2]/tbody/tr/td[3]/input[5]')

time.sleep(1)

proceedButton.click()

time.sleep(2)

submit = web.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/input')
submit.click()

time.sleep(1)


web.save_screenshot('./confirmationImg.png')


from PIL import Image

image = Image.open('confirmationImg.png')
image.show()
