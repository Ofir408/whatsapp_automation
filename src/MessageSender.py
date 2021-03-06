import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 3
WHATSAPP_URL = 'https://web.whatsapp.com/'


class MsgSender:
    def __init__(self, chrome_driver_path):
        self.driver = None
        self.chrome_driver_path = chrome_driver_path
        self.init_barcode()

    def send_whatsapp_message(self, message, contact):
        options = webdriver.ChromeOptions()
        user_dir = os.path.join(os.path.expandvars('%LocalAppData%'),
                                'Google', 'Chrome', 'User Data', 'Default')
        options.add_argument(
            f'user-data-dir={user_dir}')
        # Be careful with pushing the session to Github!!
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=options)

        self.driver.get(WHATSAPP_URL)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div/div[3]")))

        # press on the 'search contact' in whatsapp.
        search_box = self.driver.find_element_by_xpath(f'//*[@class="_2S1VP copyable-text selectable-text"]')
        time.sleep(TIMEOUT)  # seconds

        search_box.send_keys(contact)  # search the contact in the search box.
        time.sleep(TIMEOUT)  # seconds

        contact_box = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        time.sleep(TIMEOUT)  # seconds
        contact_box.click()  # to enter whatsapp chat
        textbox = self.driver.find_elements_by_xpath(f'//*[@class="_2S1VP copyable-text selectable-text"]')[-1]

        # for sending message with linebreaks
        for part in message.split('\n'):
            textbox.send_keys(part)
            ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                Keys.ENTER).perform()

        send_button = self.driver.find_element_by_class_name("_35EW6")
        send_button.click()
        time.sleep(TIMEOUT)  # seconds
        self.driver.quit()

    def init_barcode(self):
        options = webdriver.ChromeOptions()
        user_dir = os.path.join(os.path.expandvars('%LocalAppData%'),
                                'Google', 'Chrome', 'User Data', 'Default')
        options.add_argument(
            f'user-data-dir={user_dir}')
        # Be careful with pushing the session to Github!!
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=options)

        self.driver.get(WHATSAPP_URL)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div/div[3]")))
        self.driver.quit()


