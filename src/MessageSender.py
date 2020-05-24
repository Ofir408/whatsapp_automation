import sys
import os
import time

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

    def send_whatsapp_message(self, message, contact):
        options = webdriver.ChromeOptions()
        user_dir = os.path.join(os.path.expandvars('%LocalAppData%'),
                                'Google', 'Chrome', 'User Data', 'Default')
        options.add_argument(
            f'user-data-dir={user_dir}')
        # Be careful with pushing the session to Github!!
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=options)

        driver.get(WHATSAPP_URL)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div/div[3]")))

        # press on the 'search contact' in whatsapp.
        search_box = driver.find_element_by_xpath(f'//*[@class="_2S1VP copyable-text selectable-text"]')
        time.sleep(TIMEOUT)  # seconds

        search_box.send_keys(contact)  # search the contact in the search box.
        time.sleep(TIMEOUT)  # seconds

        contact_box = driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        time.sleep(TIMEOUT)  # seconds
        contact_box.click()  # to enter whatsapp chat
        textbox = driver.find_elements_by_xpath(f'//*[@class="_2S1VP copyable-text selectable-text"]')[-1]
        textbox.send_keys(message)
        send_button = driver.find_element_by_class_name("_35EW6")
        send_button.click()
        time.sleep(TIMEOUT)  # seconds

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    chrome_driver_path, contact, message = sys.argv[1:]
    msg_sender = MsgSender(chrome_driver_path=chrome_driver_path)
    msg_sender.send_whatsapp_message(message=message,
                                     contact=contact)

