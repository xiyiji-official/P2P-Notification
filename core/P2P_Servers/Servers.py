import redis
from flask import Flask


class Servers:
    def __init__(self, host, port, password, db):
        self.conn = redis.Redis(host=host,
                                port=port,
                                password=password,
                                db=db)
        self.app = Flask(__name__)
