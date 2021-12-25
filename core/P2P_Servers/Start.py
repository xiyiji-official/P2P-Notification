from concurrent.futures import ThreadPoolExecutor

from flask import Flask
from flask import request

import Show_message

app = Flask(__name__)
executor = ThreadPoolExecutor(2)


@app.route('/received', methods=["POST"])
def received():
    """
    创建了一个可以POST的接口，接受到了之后通过redis发布出去

    :return: 随便返回了点什么
    """
    data = request.get_data(cache=True).decode("UTF-8")
    print(data)
    executor.submit(Show_message.show, data)
    return "OK"


if __name__ == '__main__':
    # 外网访问：0.0.0.0，内网访问：127.0.0.1
    app.run(host="0.0.0.0", port=8888, debug=True)
