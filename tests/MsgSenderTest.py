import sys

from src.MessageSender import MsgSender

if __name__ == '__main__':
    chrome_driver_path, contact, message = sys.argv[1:]
    msg_sender = MsgSender(chrome_driver_path=chrome_driver_path)
    msg_sender.send_whatsapp_message(message=message,
                                     contact=contact)
