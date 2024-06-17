import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


class search():
    def searchInput(self):
        # Inisialisasi driver
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().geckodriver_path)
        driver = webdriver.Firefox()

        # Buka halaman Sciencedirect
        driver.get("https://muhammadiyah.or.id/")

        # Temukan elemen input pencarian
        search_icon = driver.find_element(By.XPATH,"//div[@class='jeg_midbar jeg_container jeg_navbar_wrapper normal']//a[@class='jeg_search_toggle']")
        search_icon.click()
        search_input = driver.find_element(By.XPATH, "//div[@class='jeg_midbar jeg_container jeg_navbar_wrapper normal jeg_search_expanded']//input[@placeholder='Search...']")

        # Masukkan kata kunci
        search_input.send_keys("Ketua Umum")
        time.sleep(2)

        # Klik tombol cari
        search_button = driver.find_element(By.XPATH,"//div[@class='jeg_midbar jeg_container jeg_navbar_wrapper normal jeg_search_expanded']//button[@aria-label='Search Button']")
        search_button.click()

        # # Verifikasi hasil pencarian
        # results_title = driver.find_element(By.XPATH,'//h1[normalize-space()="Search Result for 'Ketua Umum'"]')
        # assert results_title.text == "Ketua Umum"
        # // h1[normalize - space() = "Search Result for 'Ketua Umum'"]
        time.sleep(2)

        # Tutup browser
        # driver.quit()

searchByPath = search()
searchByPath.searchInput()
