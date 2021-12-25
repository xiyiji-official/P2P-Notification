# P2P-Notification

## 通过~~IFTTT~~Notification-Sender转发来在PC上接收手机通知

~~手机-->IFTTT-->开启了服务的服务器-->redis发布订阅-->pc客户端接收-->调用win弹窗通知显示~~

手机-->Notification-Sender-->pc客户端接收-->调用win弹窗通知显示

2021年12月20日：

基本解决了弹窗显示的问题，现在可以留存通知内容在通知中心里（win10、11），\
在大量消息被接收时，弹窗不会阻塞只显示第一个，并且可以按顺序连续显示。

2021年12月25日

修改了整个通知推送过程，排除了对IFTTT的依赖，由Notification-Sender（基于一个获取通知的Demo修改而来）这个app在局域网内post数据,\
并且取消了对于redis的使用，取消了对有公网IP服务器的依赖，在内网通知更容易保护隐私。


