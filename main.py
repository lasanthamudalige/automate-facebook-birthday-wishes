from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip
import os
from dotenv import load_dotenv

# load username and password from env file
load_dotenv()
FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")


def main():
    # Load chrome driver
    driver = webdriver.Chrome()

    # Load firefox driver
    #driver = webdriver.Firefox()

    driver.get("https://www.facebook.com")

    email_input_box = driver.find_element(By.NAME, "email")
    email_input_box.send_keys(FACEBOOK_EMAIL)

    password_input_box = driver.find_element(By.NAME, "pass")
    password_input_box.send_keys(FACEBOOK_PASSWORD)

    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()

	# wait for loading 
    sleep(10)

    driver.get("https://www.facebook.com/events/birthdays")
	
	# wait for loading 
    sleep(5)

    # get all birthday elements of males in birthdays page by css 'aria' label
    male_timelines = driver.find_elements(
        By.CSS_SELECTOR, "[aria-label='Write on his profile...']")

    # get all birthday elements of females in birthdays page by css 'aria' label
    female_timelines = driver.find_elements(
        By.CSS_SELECTOR, "[aria-label='Write on her profile...']")

    # add birthday message to males in the lists
    birthday_message = "Happy birthday to you 🎂"
    # copy birthday message to clipboard using pyperclip
    pyperclip.copy(birthday_message)

    if male_timelines:
        for male in male_timelines:
            # paste the birthday message
            male.send_keys(Keys.CONTROL + "v")
            # hit enter to send the message
            male.send_keys(Keys.ENTER)
            sleep(1)

    birthday_message = "Happy birthday to you 🎂"
    pyperclip.copy(birthday_message)

    if female_timelines:
        for female in female_timelines:
            female.send_keys(Keys.CONTROL + "v")
            female.send_keys(Keys.ENTER)
            sleep(1)

    # wait 15 seconds before closing
    sleep(10)
    driver.close()

    print("Successfully executed main.py")
    return 0


main()
