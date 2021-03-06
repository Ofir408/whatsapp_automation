from abc import ABC, abstractmethod


class Translation(ABC):
    """
    An abstract class for every future translation.
    """
    # Window layout
    @abstractmethod
    def get_window_layout_style(self) -> int:
        pass

    # WhatsAppAutomationFrame strings
    @abstractmethod
    def get_main_window_title(self) -> str:
        pass

    @abstractmethod
    def get_contact_column_title(self) -> str:
        pass

    @abstractmethod
    def get_date_time_column_title(self) -> str:
        pass

    @abstractmethod
    def get_cancel_button_label(self) -> str:
        pass

    @abstractmethod
    def get_schedule_new_message_button_label(self) -> str:
        pass

    # ScheduleMessageDialog Strings
    @abstractmethod
    def get_schedule_message_dialog_title(self) -> str:
        pass

    @abstractmethod
    def get_contact_input_hint(self) -> str:
        pass

    @abstractmethod
    def get_message_input_hint(self) -> str:
        pass

    @abstractmethod
    def get_date_time_input_label(self) -> str:
        pass

    @abstractmethod
    def get_schedule_message_dialog_submit_label(self) -> str:
        pass

    @abstractmethod
    def get_invalid_date_message_content(self) -> str:
        pass

    @abstractmethod
    def get_invalid_date_message_title(self) -> str:
        pass


