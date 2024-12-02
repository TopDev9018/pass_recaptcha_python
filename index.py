from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Instantiate the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Load the target page
captcha_page_url = "https://myaccount.ladwp.com/ladwp/faces/AccountSummary"
driver.get(captcha_page_url)
username_input = driver.find_element(By.NAME, "userid")  # Update with actual field name
password_input = driver.find_element(By.NAME, "password")  # Update with actual field name


username_input.send_keys("ASK_ME_FOR_THIS")  # Replace with your username
password_input.send_keys("ASK_ME_FOR_THIS")  # Replace with your password
# Solve the Captcha
print("Solving Captcha")
recaptcha_data_sitekey = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
print(recaptcha_data_sitekey)
solver = TwoCaptcha("api_key")
response = solver.recaptcha(sitekey=recaptcha_data_sitekey, url=captcha_page_url)
code = response['code']
print(f"Successfully solved the Captcha. The solve code is {code}")

# Set the solved Captcha
recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response')
driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

time.sleep(5)
# Submit the form
driver.find_element(By.NAME, "loginFrm").submit()

# Pause the execution so you can see the screen after submission before closing the driver
input("Press enter to continue")
driver.close()