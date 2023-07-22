from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Image's url that will replace the unwanted pfp
image_url = "https://media.discordapp.net/attachments/571106990726840324/1124650634981945424/image.png"


def change_image():
    # Middle part of the unwanted profile picture's link
    src_value = "284037898603462666/16d540c2044b8f53ceba3317b4e7efd4"

    # Wait until an instant of the pfp is found
    wait = WebDriverWait(driver, 9999)
    wait.until(EC.presence_of_element_located((By.XPATH, f"//img[contains(@src, '{src_value}')]")))

    # Get the unwanted elements
    elements = driver.find_elements(By.XPATH, f"//img[contains(@src, '{src_value}')]")

    # For each element, replace its src link, thus replacing the image
    for i in elements:
        driver.execute_script(f"arguments[0].src = '{image_url}';", i)


if __name__ == "__main__":
    # Get Chrome's user data, to open the Chrome instance with default settings
    # Mostly for automatically logging into discord, if logged on before
    username = os.getlogin()
    user_data_directory = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data"
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={user_data_directory}')

    # Open Chrome with discord link
    driver = webdriver.Chrome(options=options)
    driver.get("https://discord.com/channels/@me")

    # Repeatedly look for the unwanted pfp instances and replace them
    while True:
        try:
            change_image()
        except Exception as e:
            print("window has been closed, or an error has occurred")
            print(e)
            exit()
