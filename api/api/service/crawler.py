from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class Crawler:
    @classmethod
    def driver(cls): 
        service = ChromeService()
        return webdriver.Chrome(service=service)

    @classmethod
    def get(cls, url, wait=10): 
        driver = cls.driver()
        driver.get(url)

        element = WebDriverWait(driver, wait)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        driver.quit()
        return soup
        