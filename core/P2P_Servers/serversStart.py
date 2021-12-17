import os
from configparser import ConfigParser
from flask import request
from Servers import Servers

config = ConfigParser()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 读取配置文件
config.read(os.path.join(BASE_DIR, './config/config.ini'), encoding='UTF-8')

servers = Servers(host=config.get('redis', 'host'),
                  port=config.getint('redis', 'port'),
                  password=config.get('redis', 'password'),
                  db=config.getint('redis', 'db'))


@servers.app.route('/received', methods=["POST"])
def received():
    """
    创建了一个可以POST的接口，接受到了之后通过redis发布出去

    :return: 随便返回了点什么
    """
    user = request.data.decode("UTF-8")
    servers.conn.publish("notification", user)
    return "400"


if __name__ == '__main__':
    # 外网访问：0.0.0.0，内网访问：127.0.0.1
    servers.app.run(host="0.0.0.0", port=5000, debug=True)
