import os
from configparser import ConfigParser

from Client import Client

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config = ConfigParser()
# 读取配置文件
config.read(os.path.join(BASE_DIR, './config/config.ini'), encoding='UTF-8')

client = Client(host=config.get('redis', 'host'),
                port=config.getint('redis', 'port'),
                password=config.get('redis', 'password'),
                db=config.getint('redis', 'db'))
client.main()
