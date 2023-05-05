# Futuresboard Notificator
This is a simple Python script designed to fetch today’s profit from the Futuresboard webpage and send notifications to Pushbullet and ntfy.

### Configuration
To get started, copy the .env.example file to a new file called .env. Then, update the environment variables with your domain name and Pushbullet access token and/or ntfy topic name.

```
cp .env.example .env
```
```
FUTURESBOARD_URL=http://mydomain:5000
PUSHBULLET_ACCESS_TOKEN=o.0eXXXXXXXXXXXXX
NTFY_TOPIC=my-ntfy-topic
NAME=binance1
DELAY_MINUTES=60
```

### Starting
You can start the script in two ways:

#### Using host's python
```
pip3 install -r requirements.txt
python3 send_loop.py
```

#### Using docker
Alternatively, you can use Docker to run the script.
```
docker-compose up
```

### Links
- [Futuresboard](https://github.com/ecoppen/futuresboard)
- [apprise](https://github.com/caronc/apprise)
- [ntfy](https://github.com/binwiederhier/ntfy)
- [PushBullet](https://www.pushbullet.com/)

### TODO
Some features that could be added to futuresboard notificator:
- Include more notification channels such as Telegram or Discord.
- Futuresboard v2 support.
- Integrating it directly into Futuresboard itself. Or get data directly from the exchange.
