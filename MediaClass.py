import websockets
from MediaSdp import *
import json, time
import socket


async def video_play(MediaIp):
    """This is the execution function for video browsing"""

    udp_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp_port.bind(("127.0.0.1", 50668))
    udp_port.listen(10)

    #TODO ws 链接并进行 sdp 协商
    async with websockets.connect(MediaIp,ping_interval=7200,ping_timeout=14400) as ws:

        await ws.send(json.dumps({"request_id":"af9c10b2-b2ac-41c7-99b6-59a224c2fb49",
                                  "account_token":"",
                                  "cmd_type":"live",
                                  "request_type":"start",
                                  "nmedia_id":0,
                                  "callee_id":"",
                                  "device_id":"32057100001127004437",
                                  "stun_server":"",
                                  "video_resolution":"720P",
                                  "protocol":"rtp"}))
        await ws.recv()
        # await ws.recv()

        await ws.send(json.dumps({
                                    "account_token": "",
                                    "cmd_type": "ice",
                                    "request_type": "answer",
                                    "sdp": "v=0\r\n"
                                           "o=- 1631251864075308 1 IN IP4 172.16.138.60\r\n"
                                           "s=-\r\n"
                                           "t=0 0\r\n"
                                           "a=group:BUNDLE audio video\r\n"
                                           "m=audio 50668 RTP/AVP 8 111 0 103\r\n"
                                           "c=IN IP4 172.16.138.60\r\n"
                                           "a=setup:active\r\na=recvonly\r\n"
                                           "a=rtcp-mux\r\na=rtpmap:8 PCMA/8000\r\n"
                                           "a=rtpmap:111 opus/48000/2\r\na=rtcp-fb:111 transport-cc\r\n"
                                           "a=fmtp:111 minptime=10;useinbandfec=1;maxplaybackrate=16000\r\n"
                                           "a=rtpmap:103 mpeg4-generic/22050/1\r\n"
                                           "a=fmtp:103 streamtype=5;profile-level-id=1;mode=AAC-lbr;sizelength=13;indexlength=3;indexdeltalength=3;\r\n"
                                           "a=rtpmap:0 PCMU/8000\r\n"
                                           "m=video 50668 RTP/AVP 96 102 116c=IN IP4 172.16.138.60\r\n"
                                           "a=setup:active\r\n"
                                           "a=recvonly\r\n"
                                           "a=rtcp-mux\r\n"
                                           "a=rtpmap:96 H264/90000\r\n"
                                           "a=fmtp:96 level-asymmetry-allowed=1;packetization-mode=1\r\n"
                                           "a=rtcp-fb:96 nack\r\n"
                                           "a=rtcp-fb:96 nack pli\r\n"
                                           "a=rtpmap:102 HEVC/90000\r\n"
                                           "a=fmtp:102 packetization-mode=1\r\n"
                                           "a=rtcp-fb:102 nack\r\n"
                                           "a=rtcp-fb:102 nack pli\r\n"
                                }))
        await ws.recv()
        while True:
            time.sleep(10)
            heartbeat = {"account_token" : "", "cmd_type" : "detect",
                         "request_type" : "heartbeat"}
            await ws.send(json.dumps(heartbeat))
            await ws.recv()
            print(heartbeat)

def video_record():
    """This is the video recording execution function"""

    print("2")
