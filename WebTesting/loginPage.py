import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

class loginPage():
    def login(self):

        # Inisialisasi driver dengan options
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Firefox()
        driver.get("https://muhammadiyah.or.id/")

        signin_link = driver.find_element(By.XPATH, "//li[@class='sfHover']//a[@class='jeg_popuplink'][normalize-space()='Login']")
        signin_link.click()
        username_input = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_input.send_keys("syauqialfath17@gmail.com")
        # time.sleep(2)
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_input.send_keys("syauqi123")

        next_button = driver.find_element(By.XPATH, "//input[@value='Log In']")
        next_button.click()
        time.sleep(2)

loginByPath = loginPage()
loginByPath.login()