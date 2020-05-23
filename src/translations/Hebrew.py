import wx

from src.translations.Translation import Translation


class HebrewTranslation(Translation):
    """
    Hebrew translation of the GUI strings.
    """

    # Window layout
    def get_window_layout_style(self) -> int:
        return wx.Layout_RightToLeft

    # MainWindow Strings
    def get_main_window_title(self) -> str:
        return 'וואטסאפ אוטומטי'

    def get_contact_column_title(self) -> str:
        return 'איש קשר'

    def get_date_time_column_title(self) -> str:
        return 'תאריך ושעה'

    def get_cancel_button_label(self) -> str:
        return 'ביטול'

    def get_schedule_new_message_button_label(self) -> str:
        return 'הוסף הודעה'

    # ScheduleMessageDialog Strings
    def get_schedule_message_dialog_title(self) -> str:
        return 'תיזמון הודעה חדשה'

    def get_contact_input_hint(self) -> str:
        return 'הכנס/י איש קשר'

    def get_message_input_hint(self) -> str:
        return 'הכנס/י הודעה'

    def get_date_time_input_label(self) -> str:
        return 'בחר/י את תאריך ושעת ההודעה: '

    def get_schedule_message_dialog_submit_label(self) -> str:
        return 'שלח/י!'
