import os
import sys
import datetime
import threading

from datetime import datetime
from webbrowser import browser

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from src.MessageSender import MsgSender

TIMEOUT = 3
WHATSAPP_URL = 'https://web.whatsapp.com/'


class Scheduler:
    def __init__(self, chrome_driver_path):
        self.__DATE_TIME_FORMAT = '%d/%m/%Y-%H:%M:%S'
        self.scheduled_messages = {}  # dict between date:Timer in order to have the option to cancel the scheduled msg
        self.msg_sender = MsgSender(chrome_driver_path)
        self.init_barcode(chrome_driver_path)

    # schedule_date format, for example: 22/12/2020-22:30:59
    def schedule(self, schedule_date_str, msg, contact) -> bool:
        now = datetime.now()
        later_time_datetime = datetime.strptime(schedule_date_str, self.__DATE_TIME_FORMAT)
        delay = later_time_datetime - now
        print("delay type = " + str(type(delay)))
        print("delay = " + str(delay))
        seconds_to_wait = delay.total_seconds()
        print("seconds_to_wait: " + str(seconds_to_wait))

        if seconds_to_wait < 0:
            print("Invalid Date! should be later than the current date. Exit..")
            return False

        timer = threading.Timer(seconds_to_wait, self.msg_sender.send_whatsapp_message, [msg, contact])
        self.scheduled_messages[(schedule_date_str, contact)] = timer
        timer.start()
        print("the function was scheduled to date: " + schedule_date_str)
        return True

    def cancel_scheduled_msg(self, scheduled_time_str, contact):
        timer = self.scheduled_messages.pop((scheduled_time_str, contact))
        if timer is not None:
            timer.cancel()
            print("canceled successfully msg to contact= {0} at time= {1}".format(contact, scheduled_time_str))
        else:
            print("Failed to cancel msg to contact= {0} at time= {1}".format(contact, scheduled_time_str))

    def init_barcode(self, chrome_path_driver):
        options = webdriver.ChromeOptions()
        user_dir = os.path.join(os.path.expandvars('%LocalAppData%'),
                                'Google', 'Chrome', 'User Data', 'Default')
        options.add_argument(
            f'user-data-dir={user_dir}')
        # Be careful with pushing the session to Github!!
        driver = webdriver.Chrome(executable_path=chrome_path_driver, chrome_options=options)

        driver.get(WHATSAPP_URL)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div/div[3]")))
        driver.quit()


if __name__ == '__main__':
    scheduler = Scheduler(sys.argv[1:2])  # chrome path as an argument.
    scheduler.schedule("22/05/2020-23:48:40", "test", "Selenium-Test")  # TODO - change it.

    # try to cancel the scheduled task.
    # scheduler.cancel_scheduled_msg("22/05/2020-23:48:40", "Selenium-Test")
