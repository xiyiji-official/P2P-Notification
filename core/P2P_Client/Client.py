import asyncio
import time

import redis
from win10toast import ToastNotifier


class Client:
    def __init__(self, host: str, port: int, password: str, db=0):
        """
        初始化Redis对象

        :param host: redis服务器IP
        :param port: redis服务器端口
        :param password: redis服务器密码（如有）
        :param db: redis服务器的数据库（一般是0)
        """
        # 连接redis
        self.conn = redis.Redis(
            host=host,
            port=port,
            password=password,
            db=db)
        # 开启发布订阅模式
        self.pubsub = self.conn.pubsub()
        # 创建一个win10弹窗实例
        self.toaster = ToastNotifier()
        # 用来接收订阅的消息（不过貌似没啥用）
        self.msg = 0

    async def show(self, n_list):
        """
        创建一个弹窗的协程

        :param n_list: n_list为处理过的redis频道推送的内容
                       n_list内容一般为{'appName':XXXX,'title':XXXX,'message':XXXX,'time':XXXX}
        """
        message = "{},{},{}".format(n_list["appName"], n_list["title"], n_list["message"])
        print(message)
        self.toaster.show_toast(n_list["appName"],  # 弹窗标题
                                message,  # 弹窗内容
                                icon_path=None,  # 弹窗图标（None就是python的图标）
                                duration=5,  # 弹窗显示时间，在未显示完之前不会显示下一条内容
                                threaded=True)  # True不会造成阻塞

    async def recived(self):
        """
        接受订阅频道的消息并通过win10弹窗显示
        """
        self.pubsub.subscribe("notification")  # 订阅一个名为“notification”的redis频道
        while True:
            self.msg = self.pubsub.parse_response()  # 获取“notification”频道推送的内容
            print(time.strftime("%H:%M:%S", time.localtime()))
            if type(self.msg[2]) is not int:  # 由于刚刚订阅时会推送一个1的int值，所以要判断一下
                notice = eval(self.msg[2].decode('UTF-8'))  # 频道推送的内容是byte要转码
                await self.show(n_list=notice)  # 调用win10弹窗方法

    def main(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.recived())
