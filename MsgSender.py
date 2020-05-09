import time
from selenium import webdriver

TIMEOUT = 5
GOOGLE = 'https://www.google.com/'
WHATSAPP = 'https://web.whatsapp.com/'

# TODO - change it according yours.
CHROME_DRIVER_PATH = r'C:/Users/Ofir/PycharmProjects/whatsapp_automation/drivers/chromedriver_version_81.exe'


class MsgSender:

    def send_whatsapp_message(self, message, contact):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./User_Data')  # Be careful with pushing the session to Github!!
        driver = webdriver.Chrome(CHROME_DRIVER_PATH, chrome_options=options)

        driver.get(WHATSAPP)
        time.sleep(TIMEOUT * 4)  # it takes time to scan the barcode.
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
    msg_sender = MsgSender()
    msg_sender.send_whatsapp_message(message="הצלחתי!!!", contact="ברק סופשים")
