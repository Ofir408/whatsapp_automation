from abc import ABC, abstractmethod


class Translation(ABC):
    # WhatsAppAutomationFrame strings
    @abstractmethod
    def get_main_window_title(self) -> str:
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
    def get_schedule_message_dialog_submit_label(self) -> str:
        pass


