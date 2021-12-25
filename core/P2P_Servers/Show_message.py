from plyer import notification


def show(n_list):
    """
    创建一个弹窗

    :param n_list: ....
    """
    n_list = eval(n_list)
    icon = n_list["PackageName"] + ".ico"
    message = "{}\n{}\n{}".format(n_list["Title"], n_list["Text"], n_list["time"])
    print(message)
    notification.notify(title=n_list["AppName"],  # 弹窗标题
                        message=message,  # 弹窗内容
                        app_icon="./Icon/" + icon,  # 弹窗图标（None就是python的图标）
                        timeout=30,  # 弹窗显示时间
                        )
