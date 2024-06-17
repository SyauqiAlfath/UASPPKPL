import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


class englishMode():
    def english(self):
        # Inisialisasi driver
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().geckodriver_path)
        driver = webdriver.Firefox()
        driver.get("https://muhammadiyah.or.id/")

        # Temukan elemen logo sosmed
        english_icon = driver.find_element(By.XPATH,"//a[normalize-space()='EN']")
        english_icon.click()
        time.sleep(2)

        # Tutup browser
        # driver.quit()

engByPath = englishMode()
engByPath.english()
