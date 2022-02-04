from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")


driver.get("https://login.naukri.com/nLogin/Login.php")
time.sleep(3)
username= driver.find_element_by_id("usernameField")
username.send_keys("work.sharique@gmail.com")
password= driver.find_element_by_id("passwordField")
password.send_keys("Shaan@123")

time.sleep(3)
button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/div[3]/div/button[1]").click()

time.sleep(3)
driver.get("https://www.naukri.com/mnjuser/profile?id=&altresid")

#time.sleep(3)
#a= driver.find_element_by_id("attachCV")
#a.send_keys("C:\\Users\shari\Desktop\Sharique DE 1 year.pdf")