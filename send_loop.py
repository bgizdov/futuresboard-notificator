# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from futuresboard_notificator import FuturesboardNotificator

if __name__ == "__main__":
    print("Starting to send continuous notifications")
    profit_notification = FuturesboardNotificator()
    profit_notification.send_loop()