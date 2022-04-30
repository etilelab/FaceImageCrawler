from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import urllib.request

# Gender : male, female
genders = ["male", "female"]

# Hair : black, brown
hair = "black"

# Emotion :  Disgusted : 역겨운, Frightened : 겁먹은,
emotions = ['emotiondisgust','emotionangry']

# Age
# website standard age is 19.  Result age is 19 +- age_number
age_number = random.randrange(-4, 40)

# Download image count
count = 0
max_count = 300  # count (1) = gender(2) + emotion(2)
person_count = 0 # same gender

# ===================================================
# Get url
URL = 'https://generated.photos/face-generator/new'
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

time.sleep(3)  # wait 3 seconds

for i in range(0, max_count):
    for gender in genders:
        hair_count = random.randrange(1,3)
        # Set gender
        if gender == "male":
            driver.find_element_by_id("sexmale").click()
            slider = driver.find_element_by_xpath('//*[@id="hairLengthSlider"]/input')
            for i in range(hair_count):
                slider.send_keys(Keys.LEFT)
        else:
            driver.find_element_by_id("sexfemale").click()
            # Set Hair
            slider = driver.find_element_by_xpath('//*[@id="hairLengthSlider"]/input')
            for i in range(3):
                slider.send_keys(Keys.RIGHT)

        skins = ['skin#E8BA93','skin#E2956E']
        driver.find_element_by_id(skins[random.randrange(0,2)]).click()

        # Set emotion-> update face image
        for emotion in emotions:
            # Set emotion
            driver.find_element_by_id(emotion).click()

            # Update face image
            driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/aside/div[3]/div[2]/button').click()
            time.sleep(7)

            face_image = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/main/div[2]/div[1]/img').get_attribute('src')
            urllib.request.urlretrieve(face_image, "FACE_{gender}_{hair}_{emotion}_{person_count}_{count}.jpg".format(gender=gender, hair=hair, emotion=emotion, person_count=person_count,count=count))
            count = count + 1
        person_count = person_count + 1

    # Generate new image
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/aside/div[3]/div[3]/button').click()
    time.sleep(5)

    if count == max_count:
        break
