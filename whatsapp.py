import time
from selenium import webdriver

TIMEOUT = 5
GOOGLE = 'https://www.google.com/'
WHATSAPP = 'https://web.whatsapp.com/#'

# TODO - change it according yours.
CHROME_DRIVER_PATH = r'C:/Users/Ofir/PycharmProjects/whatsapp_automation/drivers/chromedriver_version_81.exe'


def send_whatsapp_message(message, contact):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get(WHATSAPP)

    time.sleep(TIMEOUT * 2)  # it takes time to scan the barcode.
    search_box = driver.find_element_by_xpath(f'//*[@title="{contact}"]')
    time.sleep(TIMEOUT)  # seconds
    search_box.click()  # to enter whatsapp chat
    textbox = driver.find_elements_by_xpath(f'//*[@class="_2S1VP copyable-text selectable-text"]')[-1]
    textbox.send_keys(message)
    send_button = driver.find_element_by_class_name("_35EW6")
    send_button.click()
    time.sleep(15)  # seconds
    driver.quit()


if __name__ == '__main__':
    send_whatsapp_message(message="הצלחתי!!!", contact="ברק סופשים")
