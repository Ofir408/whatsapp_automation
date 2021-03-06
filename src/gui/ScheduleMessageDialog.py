import wx
import wx.adv

from src.Scheduler import Scheduler
from src.translations.Translation import Translation


class ScheduleMessageDialog(wx.Dialog):
    """
    The popup to show when inserting a new message.
    """

    def __init__(self,
                 parent,
                 translation: Translation,
                 scheduler: Scheduler):
        """
        Create the popup
        :param parent: The creator frame of the popup
        :param translation: The Translation object to use strings from.
        :param scheduler: The Scheduler to use.
        """
        super(ScheduleMessageDialog, self).__init__(parent=parent,
                                                    title=translation.get_schedule_message_dialog_title())
        self.scheduler = scheduler
        self.translation = translation

        # Set language appropriate layout
        self.SetLayoutDirection(translation.get_window_layout_style())

        self.main_panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.date_time_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Inputs
        self.contact_input = wx.TextCtrl(self.main_panel)
        self.contact_input.SetHint(translation.get_contact_input_hint())
        self.message_input = wx.TextCtrl(self.main_panel,
                                         style=wx.TE_MULTILINE)
        self.message_input.SetHint(translation.get_message_input_hint())

        # Date & time pickers
        self.date_time_panel = wx.Panel(self.main_panel)
        self.date_time_label = wx.StaticText(self.date_time_panel,
                                             label=translation.get_date_time_input_label())
        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.date_time_label.SetFont(font)
        self.date_picker = wx.adv.DatePickerCtrl(self.date_time_panel)
        self.time_picker = wx.adv.TimePickerCtrl(self.date_time_panel)

        self.date_time_sizer.Add(self.date_time_label, 1, wx.EXPAND)
        self.date_time_sizer.AddStretchSpacer()
        self.date_time_sizer.Add(self.date_picker)
        self.date_time_sizer.Add(self.time_picker)
        self.date_time_panel.SetSizer(self.date_time_sizer)

        # Submit button
        self.submit_btn = wx.Button(self.main_panel,
                                    label=translation.get_schedule_message_dialog_submit_label())
        self.submit_btn.Bind(wx.EVT_BUTTON, self.on_click)

        # Capture ENTER key
        self.submit_btn.SetDefault()

        # Arrange on screen
        self.main_sizer.Add(self.contact_input, 0, wx.EXPAND)
        self.main_sizer.Add(self.message_input, 1, wx.EXPAND)
        self.main_sizer.Add(self.date_time_panel)
        self.main_sizer.Add(self.submit_btn, 0, wx.CENTER)

        self.main_panel.SetSizer(self.main_sizer)

    def on_click(self, event):
        """
        An event that will be triggered when clicking the 'Submit' button.
        :param event: The click event
        """
        if self._submit():
            self.Close()

    def _submit(self) -> bool:
        """
        Inner submit function:
        Extracts the new message's parameters and schedules it.
        """
        contact = str(self.contact_input.Value)
        message = str(self.message_input.Value)

        date = self.date_picker.Value.Format('%d/%m/%Y')
        time = self.time_picker.Value.Format('%H:%M:%S')
        date_time = f'{date}-{time}'

        res = self.scheduler.schedule(date_time,
                                      message,
                                      contact)
        if not res:
            wx.MessageBox(self.translation.get_invalid_date_message_content(),
                          self.translation.get_invalid_date_message_title(),
                          wx.OK | wx.ICON_ERROR)

        return res
