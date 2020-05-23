import argparse
import wx

from src.Scheduler import Scheduler
from src.gui.ScheduleMessageDialog import ScheduleMessageDialog
from src.translations.Translation import Translation
from src.translations.TranslationFactory import TranslationFactory


class WhatsAppAutomationFrame(wx.Frame):
    def __init__(self,
                 translation: Translation,
                 scheduler: Scheduler):
        super(WhatsAppAutomationFrame, self).__init__(parent=None,
                                                      title=translation.get_main_window_title())
        self.translation = translation
        self.scheduler = scheduler

        # Set language appropriate layout
        self.SetLayoutDirection(translation.get_window_layout_style())

        self.main_panel = wx.Panel(self)
        self.btn = wx.Button(self.main_panel,
                             label=translation.get_schedule_new_message_button_label())
        self.btn.Bind(wx.EVT_BUTTON, self.on_click)

        self.Show()

    def on_click(self, event):
        popup = ScheduleMessageDialog(self,
                                      self.translation,
                                      self.scheduler)
        popup.Show()


def parse_arguments() -> argparse.Namespace:
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
    frame = WhatsAppAutomationFrame(translation, scheduler)

    app.MainLoop()


if __name__ == '__main__':
    main()
