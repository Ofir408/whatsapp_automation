import sys
import datetime
import threading

from datetime import datetime

from src.message_sender import MsgSender


class Scheduler:
    def __init__(self, chrome_driver_path):
        self.__DATE_TIME_FORMAT = '%d/%m/%Y-%H:%M:%S'
        self.scheduled_messages = {}  # dict between date:Timer in order to have the option to cancel the scheduled msg
        self.msg_sender = MsgSender(chrome_driver_path)

    # schedule_date format, for example: 22/12/2020-22:30:59
    def schedule(self, schedule_date_str, msg, contact):
        now = datetime.now()
        later_time_datetime = datetime.strptime(schedule_date_str, self.__DATE_TIME_FORMAT)
        delay = later_time_datetime - now
        print("delay type = " + str(type(delay)))
        print("delay = " + str(delay))
        seconds_to_wait = delay.total_seconds()
        print("seconds_to_wait: " + str(seconds_to_wait))

        if seconds_to_wait < 0:
            print("Invalid Date! should be later than the current date. Exit..")
            exit(1)

        timer = threading.Timer(seconds_to_wait, self.msg_sender.send_whatsapp_message, [msg, contact])
        self.scheduled_messages[(schedule_date_str, contact)] = timer
        timer.start()
        print("the function was scheduled to date: " + schedule_date_str)

    def cancel_scheduled_msg(self, scheduled_time_str, contact):
        timer = self.scheduled_messages.get((scheduled_time_str, contact))
        if timer is not None:
            timer.cancel()
            print("canceled successfully msg to contact= {0} at time= {1}".format(contact, scheduled_time_str))

        else:
            print("Failed to cancel msg to contact= {0} at time= {1}".format(contact, scheduled_time_str))


if __name__ == '__main__':
    scheduler = Scheduler(sys.argv[1:2])  # chrome path as an argument.
    scheduler.schedule("22/05/2020-23:48:40", "test", "Selenium-Test")  # TODO - change it.

    # try to cancel the scheduled task.
    #scheduler.cancel_scheduled_msg("22/05/2020-23:48:40", "Selenium-Test")

