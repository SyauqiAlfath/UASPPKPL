import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


class socialMedia1():
    def socmed_x(self):
        # Inisialisasi driver
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().geckodriver_path)
        driver = webdriver.Firefox()
        driver.get("https://muhammadiyah.or.id/")

        # Temukan elemen logo sosmed
        x_icon = driver.find_element(By.XPATH,"//div[@class='jeg_nav_item socials_widget jeg_social_icon_block nobg']//a[@class='jeg_twitter']")
        x_icon.click()
        time.sleep(2)

        # Tutup browser
        # driver.quit()

socmedByPath = socialMedia1()
socmedByPath.socmed_x()
