import wx

from src.translations.Translation import Translation


class EnglishTranslation(Translation):
    """
    English translation of the GUI strings.
    """
    # Window layout
    def get_window_layout_style(self) -> int:
        return wx.Layout_LeftToRight

    # MainWindow Strings
    def get_main_window_title(self) -> str:
        return 'WhatsApp Automation'

    def get_contact_column_title(self) -> str:
        return 'Contact'

    def get_date_time_column_title(self) -> str:
        return 'Date & Time'

    def get_cancel_button_label(self) -> str:
        return 'Cancel'

    def get_schedule_new_message_button_label(self) -> str:
        return 'Add message'

    # ScheduleMessageDialog Strings
    def get_schedule_message_dialog_title(self) -> str:
        return 'Schedule a new message'

    def get_contact_input_hint(self) -> str:
        return 'Enter contact'

    def get_message_input_hint(self) -> str:
        return 'Enter message'

    def get_date_time_input_label(self) -> str:
        return 'Select message time and date: '

    def get_schedule_message_dialog_submit_label(self) -> str:
        return 'Submit!'

    def get_invalid_date_message_content(self) -> str:
        return 'Please select a future date.'

    def get_invalid_date_message_title(self) -> str:
        return 'Invalid date!'
