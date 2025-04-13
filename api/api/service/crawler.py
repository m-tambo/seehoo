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
        service = ChromeService(executable_path='/usr/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=service, options=options)

    @classmethod
    def get(cls, url, wait=10): 
        driver = cls.driver()
        driver.get(url)

        element = WebDriverWait(driver, wait)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        driver.quit()
        return soup
        