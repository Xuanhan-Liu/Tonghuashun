import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform


class Selenium_Handler:
    def __init__(self, driver_path, headless=True, file_path='./config/ua.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.UAs = file.read().split('\n')
        idx = random.randint(0, len(self.UAs))
        options = Options()
        options.add_argument(
            'user-agent=' + self.UAs[idx])
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        if headless:
            options.add_argument('--headless')
        if platform.system().lower() == 'linux':
            options.add_argument("--no-sandbox")  # linux only
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("–disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(executable_path=driver_path,
                                       options=options)
        self.driver.set_window_size(1366, 768)
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {
            "User-Agent": self.UAs[idx]}})
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => false
                    })
                """
        })
        with open('stealth.min.js', 'r') as f:
            js = f.read()
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
        self.driver.execute_cdp_cmd("Page.removeScriptToEvaluateOnNewDocument", {"identifier": "1"})

    def load_content(self, url, key_element):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, key_element)))
        page_source = self.driver.page_source
        self.driver.quit()
        return page_source

    def slider_load(self, url, element, element_size, offset_width):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH, element)))
        slider_loc = button.location_once_scrolled_into_view
        slider_size = element_size
        start_x = slider_loc['x'] + slider_size[0] / 2
        end_x = start_x + offset_width
        slider_action = ActionChains(self.driver)
        slider_action.move_to_element(button)
        slider_action.click_and_hold().perform()
        # for i in range(int(end_x - start_x) // 30):
        #     slider_action.move_by_offset(i * 30, 0).pause(0.01)
        slider_action.move_by_offset(offset_width, 0).perform()
        slider_action.release().perform()

        page_source = self.driver.page_source
        self.driver.quit()
        return page_source
