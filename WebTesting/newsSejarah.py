import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


class newsSejarah():
    def sejarah(self):
        # Inisialisasi driver
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().geckodriver_path)
        driver = webdriver.Firefox()
        driver.get("https://muhammadiyah.or.id/")

        # Temukan elemen logo sosmed
        sejarah_icon = driver.find_element(By.XPATH,"//div[contains(@class,'jeg_midbar jeg_container jeg_navbar_wrapper normal')]//a[normalize-space()='SEJARAH']")
        sejarah_icon.click()
        time.sleep(2)

        # Tutup browser
        # driver.quit()

newsByPath = newsSejarah()
newsByPath.sejarah()
