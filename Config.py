import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13595786"))
    API_HASH = os.environ.get("API_HASH", "e326248b4b66384f067f6b18f98c0030")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5383212480:AAHguTVAsKDfC0FgBDD9WuCo761rkMtwh6M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AgAOMTQ5LjE1NC4xNjcuNTEBu1kCvD8598vitVB83z3KUeENj2Y1tXeplQc5GyB8CE8RRUqW0qQaG3gU0FcYv+WmJrturziIsxRy4mO7mr8dpMrTWIfSsmLQsIrxdQ35e/W9tftOVdp6xOZznFr4CsOY7Fkbo9UB9vGE/2isKJTgH2J+UUlgoQ2N+9pRLmtrcKM8ao7afh1M+Q+T6sGuOUb/3brp/Z1a4AnlIh3LV+6ShB/EVRQHrIMIzuR1u8NY9zVKaCy/+8MF9vqkZXfb3e5B26IJbUX5mQtge/+3RQ0XKkR2TRogXI97kx1GvYcq1B/yCE8+ummjP8u4vsUEd+2eHk9CkT4549XN4xHau/blJZk")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "bzkzbot")
    SUPPORT = os.environ.get("SUPPORT", "WW49W")
    CHANNEL = os.environ.get("CHANNEL", "WW49W")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
