import sys

from src.Scheduler import Scheduler

if __name__ == '__main__':
    scheduler = Scheduler(sys.argv[1:2])  # chrome path as an argument.
    scheduler.schedule("22/05/2020-23:48:40", "test", "Selenium-Test")  # TODO - change it.

    # try to cancel the scheduled task.
    scheduler.cancel_scheduled_msg("22/05/2020-23:48:40", "Selenium-Test")
