from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import urllib.request

# Gender : male, female
gender = "male"

# Hair : black, brown
hair = "black"

# Emotion :  Disgusted : 역겨운, Frightened : 겁먹은,
emotion_dict = {'disgust':'emotiondisgust','angry':'emotionneangry'}
emotion = emotion_dict['disgust']

# Age
# website standard age is 19.  Result age is 19 +- age_number
age_number = random.randrange(-4, 25)

# Download image count
count = 0

# ===================================================
# Get url
URL = 'https://generated.photos/face-generator/6268f6b0f44734000f062f19'
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

time.sleep(3)  # wait 3 seconds

# Gender click
if gender == "male":
    driver.find_element_by_id("sexmale").click()
else:
    driver.find_element_by_id("sexfemale").click()

# Hair click
if hair == "black":
    driver.find_element_by_id("hair#404040").click()
elif hair == "brown":
    driver.find_element_by_id("hair#6C4F3D").click()

# Emotion click
driver.find_element_by_id(emotion).click()

# Age range
slider = driver.find_element_by_xpath('//*[@id="ageSlider"]/input')
if age_number > 0:
    for i in range(age_number):
      slider.send_keys(Keys.RIGHT)
else:
    for i in range(age_number):
      slider.send_keys(Keys.LEFT)

# Update face image
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/aside/div[3]/div[2]/button').click()
time.sleep(7)

face_image = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/main/div[2]/div[1]/img').get_attribute('src')
urllib.request.urlretrieve(face_image, "FACE_{gender}_{hair}_{emotion}_{count}.jpg".format(gender=gender, hair=hair, emotion=emotion, count=count))
count = count + 1

# Generate new image
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/aside/div[3]/div[3]/button').click()