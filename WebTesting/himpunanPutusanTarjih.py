import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


class himpunanPutusanTarjih():
    def tarjih(self):
        # Inisialisasi driver
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().geckodriver_path)
        driver = webdriver.Firefox()
        driver.get("https://muhammadiyah.or.id/")

        # Temukan elemen logo sosmed
        tarjih_button = driver.find_element(By.XPATH,"//a[@href='https://tarjih.or.id']")
        tarjih_button.click()
        time.sleep(2)

        # Tutup browser
        # driver.quit()

tarjihByPath = himpunanPutusanTarjih()
tarjihByPath.tarjih()
