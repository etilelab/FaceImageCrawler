import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

# gender : male, female
gender = "male"

# hair : black, brown
hair = "black"

# emotion :  Disgusted : 역겨운, Frightened : 겁먹은,
emotion_dict = {'disgust':'emotiondisgust','angry':'emotionneangry'}
emotion = emotion_dict['disgust']

# get url
URL = 'https://generated.photos/face-generator/6268f6b0f44734000f062f19'
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

time.sleep(5)  # wait 5 seconds

# gender click
if gender == "male":
    driver.find_element_by_id("sexmale").click()
else:
    driver.find_element_by_id("sexfemale").click()

# hair click
if hair == "black":
    driver.find_element_by_id("hair#404040").click()
elif hair == "brown":
    driver.find_element_by_id("hair#6C4F3D").click()

# emotion click
driver.find_element_by_id(emotion).click()

