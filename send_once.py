# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from futuresboard_notificator import FuturesboardNotificator

if __name__ == "__main__":
    print("Starting to send one notification")
    profit_notification = FuturesboardNotificator()
    profit_notification.get_todays_profit()
    profit_notification.send_notification()