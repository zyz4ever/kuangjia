import configparser
import MediaClass
import asyncio

# 定义常量 读取配置文件
application = configparser.ConfigParser()
application.read("./application.ini")

def VideoPlayConfig():
    """This is a function about the video viewing read configuration"""

    # 读取配置文件流媒体地址端口并向 MediaClass.video_play 传参
    MediaIp1 = application.get("nmedia", "nmedia_ip")
    MediaIp = "ws://" + MediaIp1

    # 判断并确认是否执行视频浏览
    if int(application.get("ws", "Video_Play")) > 0:
        play_key = application.options("ws")
        for Executive in play_key:
            eval('asyncio.run(MediaClass.%s(MediaIp))' % Executive)

def VideoRecord():
    """This is a function about video recording read configuration"""

    # 判断并确认是否执行录像
    if int(application.get("record", "Video_Record")) > 0:
        record_key = application.options("record")
        for Executive in record_key:
            eval('MediaClass.%s()' % Executive)