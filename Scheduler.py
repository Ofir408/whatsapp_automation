import datetime
from datetime import datetime
import threading

from MsgSender import MsgSender


class Scheduler:

    def __init__(self):
        self.__DATE_TIME_FORMAT = '%d/%m/%Y-%H:%M:%S'
        self.msg_sender = MsgSender()

    # schedule_date format, for example: 22/12/2020-22:30:59
    def scheduler_func(self, schedule_date_str, msg, contact):
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

        threading.Timer(seconds_to_wait, msgSender.send_whatsapp_message, [msg, contact]).start()
        print("the function was scheduled to date: " + schedule_date_str)


if __name__ == '__main__':
    scheduler = Scheduler()
    msgSender = MsgSender()
    scheduler.scheduler_func("10/06/2020-19:37:20", "test", "ברק סופשים")  # TODO - change it.

