from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from ReservationFood_PATH import get_PATH

username_Person = input("Enter your student cod: ")
password_Person = input("Enter your password: ")
date = input("Enter your date: ")

driver = webdriver.Firefox()
print(type(driver))
# driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://erp.bzte.ac.ir/Dashboard")

sleep(10)
driver.switch_to.frame(1)
# print("avaz shod")
elm = driver.find_element(By.XPATH,get_PATH("dashbord", "vorodBeSamane"))
# print("ta inja omade")
elm.click()


driver.switch_to.default_content()
iframe = driver.find_element(By.ID,"iframe_4149")
driver.switch_to.frame(iframe)
print("kheir nabini")
username = driver.find_element(By.ID,get_PATH("login_page","username"))
username.send_keys(username_Person)
print("username ja gozari shod ")
password = driver.find_element(By.ID,get_PATH("login_page", "password"))
password.send_keys(password_Person)
print("password vared shod")
login = driver.find_element(By.XPATH,get_PATH("login_page", "vorod"))
login.click()

sleep(2)
driver.switch_to.default_content()
elm = driver.find_element(By.XPATH,get_PATH("user_panel", "tabligh"))
elm.click()
sleep(1)
# ta inja varede safhe asli shodim

# TODO: vared shodan be safhe rezerv ghaza
driver.switch_to.frame(1)
driver.find_element(By.XPATH,get_PATH("user_panel", "omorTaghzie")).click()
driver.find_element(By.XPATH,get_PATH("omorTaghzie", "rezervGhaza")).click()

# TODO: moshkel baz shodan ghesmat rezerv ghaza
# if driver.find_element(By.XPATH,"/html/body/div/div"):
#     print("sit baz moshkel dare ie vaght dige emtehan kon")
#     exit()

# TODO : entekhab vade nahar 
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.ID,get_PATH("rezervGhaza", "rezervGhaza_frame")))
sleep(2)
driver.find_element(By.XPATH,get_PATH("rezervGhaza" , "male_list")).click()
driver.find_element(By.XPATH,get_PATH("rezervGhaza", "select_diner")).click()
food = driver.find_element(By.XPATH,"//input[contains(@onclick,'%s')]" % date)
food.click()

# TODO : kharid qaza
driver.switch_to.default_content()
iframe = driver.find_element(By.XPATH,"//*[@id='iframe_New_DinerSaleDate_Tab']")
driver.switch_to.frame(iframe)
food = driver.find_element(By.XPATH,"/html/body/form/div[3]/div[1]/div/div[5]/input")
food.click()
iframe = driver.find_element(By.XPATH,"//*[@id='Add_iframe']")
food = driver.find_element(By.XPATH,"/html/body/form/div[3]/input")
food.click()