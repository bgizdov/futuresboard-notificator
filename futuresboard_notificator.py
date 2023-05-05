# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import time
import apprise
import urllib3
from bs4 import BeautifulSoup
from dotenv import dotenv_values

class FuturesboardNotificator:
    def __init__(self):
        self.todays_profit = 0
        self.config = dotenv_values(".env")
        # Create an Apprise instance
        self.apobj = apprise.Apprise()
        #  pushbullet notification
        notification_services = 0
        if 'PUSHBULLET_ACCESS_TOKEN' in self.config:
            self.apobj.add(f"pbul://{self.config['PUSHBULLET_ACCESS_TOKEN']}")
            notification_services += 1
            print("Pushbullet notification service configured")
        if 'NTFY_TOPIC' in self.config:
            self.apobj.add(f"ntfy://{self.config['NTFY_TOPIC']}")
            notification_services += 1
            print("Ntfy notification service configured")
        if notification_services == 0:
            print("Error: No notification services configured")
            exit(1)
        self.delay = 60 * int(self.config['DELAY_MINUTES'])
        print("ProfitNotification initialized")

    def get_todays_profit(self):
        web_page = urllib3.request("GET", self.config['FUTURESBOARD_URL']).data
        soup = BeautifulSoup(web_page, "html.parser")
        profit = soup.find('p', {'class': 'card-text'}).contents
        todays_profit = profit[0]
        self.todays_profit = todays_profit
        print("Todays profit: " + todays_profit)
        return todays_profit

    def send_notification(self):
        body = f'Todays profit: {self.todays_profit}'
        name = self.config['NAME']
        title = f'Todays profit {name}'
        self.apobj.notify(
            body=body,
            title=title)
        print("Notification sent")

    def send_loop(self):
        print("Starting to send continuous notifications")
        while True:
            old_profit = self.todays_profit
            self.todays_profit = self.get_todays_profit()
            if old_profit != self.todays_profit:
                self.send_notification()
            else:
                print("No changes in profit to notify")
            time.sleep(self.delay)
