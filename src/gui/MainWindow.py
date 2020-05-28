import argparse
import locale
import wx

from wx.lib.agw import ultimatelistctrl as ulc

from src.Scheduler import Scheduler
from src.gui.ScheduleMessageDialog import ScheduleMessageDialog
from src.translations.Translation import Translation
from src.translations.TranslationFactory import TranslationFactory


class WhatsAppAutomationFrame(wx.Frame):
    """
    The main window.
    """

    def __init__(self,
                 translation: Translation,
                 scheduler: Scheduler):
        """
        Create the window.
        :param translation: The Translation object to use strings from.
        :param scheduler: The Scheduler to use.
        """
        super(WhatsAppAutomationFrame, self).__init__(parent=None,
                                                      title=translation.get_main_window_title())
        self.translation = translation
        self.scheduler = scheduler

        # Set language appropriate layout
        self.SetLayoutDirection(translation.get_window_layout_style())

        self.main_panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Existing messages list
        self.messages_list = ulc.UltimateListCtrl(self.main_panel,
                                                  agwStyle=wx.LC_REPORT
                                                           | wx.LC_VRULES
                                                           | wx.LC_HRULES
                                                           | ulc.ULC_HAS_VARIABLE_ROW_HEIGHT)
        self.messages_list.InsertColumn(0,
                                        translation.get_contact_column_title(),
                                        width=150)
        self.messages_list.InsertColumn(1,
                                        translation.get_date_time_column_title(),
                                        width=150)
        self.messages_list.InsertColumn(2, '', width=80)

        # Insertion button
        self.new_message_btn = wx.Button(self.main_panel,
                                         label=translation.get_schedule_new_message_button_label())
        self.new_message_btn.Bind(wx.EVT_BUTTON, self.on_click)

        # Capture ENTER key
        self.new_message_btn.SetDefault()

        # Arrange on screen
        self.main_sizer.Add(self.messages_list, 1, wx.ALL | wx.EXPAND)
        self.main_sizer.Add(self.new_message_btn, 0, wx.CENTER)

        self.main_panel.SetSizer(self.main_sizer)

        # Insertion popup
        self.popup = None

        self.Show()

    def on_click(self, event):
        """
        An event that will be triggered when clicking the 'Add message' button.
        :param event: The click event
        """
        self.popup = ScheduleMessageDialog(self,
                                           self.translation,
                                           self.scheduler)
        self.popup.Bind(wx.EVT_CLOSE, self._update_list)

        self.popup.Show()

    def _update_list(self, *args):
        """
        Update the scheduled messages list.
        """
        self.messages_list.DeleteAllItems()

        for date_time, contact in self.scheduler.scheduled_messages.keys():
            idx = self.messages_list.InsertStringItem(0, contact)
            self.messages_list.SetStringItem(idx, 1, date_time)
            item_btn = wx.Button(self.messages_list,
                                 label=self.translation.get_cancel_button_label())
            item_btn.Bind(wx.EVT_BUTTON, self._create_item_removal_func(contact,
                                                                        date_time))
            self.messages_list.SetItemWindow(idx, 2, item_btn)

        if self.popup is not None:
            self.popup.Destroy()
            self.popup = None

    def _create_item_removal_func(self, contact: str, date_time: str):
        """
        Create a bindable function to remove a message.
        :param contact: The contact of the scheduled message
        :param date_time: The date&time string of the scheduled message
        :return: The removal function
        """
        def remove_item(event):
            self.scheduler.cancel_scheduled_msg(date_time,
                                                contact)
            self._update_list()

        return remove_item


def parse_arguments() -> argparse.Namespace:
    """
    Parse the CLI arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang', type=str,
                        help='The language to show the GUI in.',
                        default='Default')
    parser.add_argument('-p', '--path', type=str,
                        help='The path to the Chrome driver.',
                        default='drivers/chromedriver_version_81.exe')

    return parser.parse_args()


def main():
    args = parse_arguments()
    translation = TranslationFactory.get_translation(args.lang)
    scheduler = Scheduler(args.path)

    app = wx.App()

    # Fix datetime.strptime issue
    locale.setlocale(locale.LC_ALL, 'C')

    _ = WhatsAppAutomationFrame(translation, scheduler)

    app.MainLoop()


if __name__ == '__main__':
    main()
