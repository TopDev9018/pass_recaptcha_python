Let's imagine you need to resolve a CAPTCHA, for example, to submit a form. We'll do that with a popular service called 2captcha to handle CAPTCHA in Selenium using a demo page.

We'll explore how the service works against a popular CAPTCHA challenge. So, let's get started by installing some dependencies. If you don't have them yet, run the command pip install selenium 2captcha-python and import some modules as shown below.

Note: In the past, installing WebDriver was a mandatory step, but this is no longer the case. Selenium version 4 and higher come with WebDriver built-in by default. If you have an older Selenium version, upgrading is recommended to access the latest features and capabilities. You can check your current version with the command pip show selenium and update to the latest version using pip install --upgrade selenium.

program.py
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium import webdriver
import time
Then, open a Chrome instance and navigate to the demo page.

program.py
driver = webdriver.Chrome()
url = "https://2captcha.com/demo/normal"
driver.get(url)

The next step is to locate the CAPTCHA image and pass its URL to the solver.normal() method, which returns the text solution. Save it in the result variable.

program.py
imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'_2hXzbgz7SSP0DXCyvKWcha')]") 
solver = TwoCaptcha(Your_2Captcha_API_key)
result=solver.normal(imgResults[0].get_attribute('src'))
print ('solved: ' + str(result))
The following task is to find the input field, fill it with the solution text received by the 2Captcha service, and click the submit button.

program.py
captchafield = driver.find_element(By.XPATH,"//input[contains(@class,'_26Pq0m_qFk19UXx1w0U5Kv')]")
captchafield.send_keys(result['code'])

button = driver.find_element(By.XPATH,"//button[contains(@class, 'l2z7-tVRGe-3sq5kU4uu5 _2xjDiWmBxfqem8nGQMmGci _2HIb5VBFp6Oi5_JoLdEcl6 _2vbG_IBm-DpI5KeEAHJkRy')]")
button.click()
time.sleep(10)
To end, locate the <p> element on the page and print its message. You should get ''Captcha is passed successfully!'' in case of success.

program.py
messagefield=driver.find_element(By.XPATH,"//p[contains(@class,'_2WOJoV7Dg493S8DW_GobSK')]")
print (messagefield.text)
Here's the complete code:

program.py
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://2captcha.com/demo/normal"
driver.get(url)

imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'_2hXzbgz7SSP0DXCyvKWcha')]") 
solver = TwoCaptcha(Your_2Captcha_API_key)
result = solver.normal(imgResults[0].get_attribute("src"))
print ("solved: " + str(result))

captchafield = driver.find_element(By.XPATH,"//input[contains(@class,'_26Pq0m_qFk19UXx1w0U5Kv')]")
captchafield.send_keys(result["code"])

button = driver.find_element(By.XPATH,"//button[contains(@class, 'l2z7-tVRGe-3sq5kU4uu5 _2xjDiWmBxfqem8nGQMmGci _2HIb5VBFp6Oi5_JoLdEcl6 _2vbG_IBm-DpI5KeEAHJkRy')]")
button.click()
time.sleep(10)

messagefield=driver.find_element(By.XPATH,"//p[contains(@class,'_2WOJoV7Dg493S8DW_GobSK')]")
print (messagefield.text)
And here's the output:

Output
solved: {'captchaId': '72848141048', 'code': 'W9H5K'}
Captcha is passed successfully!
Congratulations! You solved your first CAPTCHA with Selenium and 2Captcha.

However, using paid solvers is hard to scale up since it's expensive and slow, and they only work with a fraction of all CAPTCHA types. Therefore, let's see an alternative next.
