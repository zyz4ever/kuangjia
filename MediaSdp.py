import json


def start():
    json = {
            "request_id" : "461648d3-5aea-4d3b-bbff-5975b6f683b1",
            "account_token" : "",
            "cmd_type" : "live",
            "request_type" : "start",
            "nmedia_id" : 0,
            "callee_id" : "",
            "device_id" : "31020000001320000001",
            "stun_server" : "",
            "video_resolution" : "720P"
        }

def answer():
    json = {
        "account_token":"",
        "cmd_type":"ice",
        "request_type":"answer",
        "sdp":
        "v=0""\r\n"
        "o=- 9029458616416951284 2 IN IP4 127.0.0.1\r\n"
        "s=-\r\nt=0 0\r\n"
        "a=group:BUNDLE audio video\r\n"
        "a=msid-semantic: WMS\r\n"
        "m=audio 9 RTP/SAVPF 8 111 0\r\n"
        "c=IN IP4 0.0.0.0\r\n"
        "a=rtcp:9 IN IP4 0.0.0.0\r\n"
        "a=ice-ufrag:Gq2s\r\n"
        "a=ice-pwd:lVB5xA5Gm1TYnocv4Sf6HRch\r\n"
        "a=ice-options:trickle\r\n"
        "a=fingerprint:sha-256 5A:91:06:3B:98:81:26:B0:59:BE:4A:F0:76:47:AC:BB:FF:F2:27:DA:F4:38:C3:5E:89:1F:B4:18:61:99:82:00\r\n"
        "a=setup:active\r\n"
        "a=mid:audio\r\n"
        "a=recvonly\r\n"
        "a=rtcp-mux\r\n"
        "a=rtpmap:8 PCMA/8000\r\n"
        "a=rtpmap:111 opus/48000/2\r\n"
        "a=rtcp-fb:111 transport-cc\r\n"
        "a=fmtp:111 minptime=10;useinbandfec=1\r\n"
        "a=rtpmap:0 PCMU/8000\r\n"
        "m=video 9 RTP/SAVPF 96\r\n"
        "c=IN IP4 0.0.0.0\r\na=rtcp:9 IN IP4 0.0.0.0\r\n"
        "a=ice-ufrag:Gq2s\r\n"
        "a=ice-pwd:lVB5xA5Gm1TYnocv4Sf6HRch\r\n"
        "a=ice-options:trickle\r\n"
        "a=fingerprint:sha-256 5A:91:06:3B:98:81:26:B0:59:BE:4A:F0:76:47:AC:BB:FF:F2:27:DA:F4:38:C3:5E:89:1F:B4:18:61:99:82:00\r\n"
        "a=setup:active\r\n"
        "a=mid:video\r\n"
        "a=extmap:5 http://www.ietf.org/id/draft-holmer-rmcat-transport-wide-cc-extensions-01\r\n"
        "a=recvonly\r\n"
        "a=rtcp-mux\r\n"
        "a=rtpmap:96 H264/90000\r\n"
        "a=rtcp-fb:96 transport-cc\r\n"
        "a=rtcp-fb:96 nack\r\n"
        "a=rtcp-fb:96 nack pli\r\n"
        "a=fmtp:96 level-asymmetry-allowed=1;packetization-mode=1;profile-level-id=42e01f\r\n",
        }

def candidate():
    json = {
        "account_token": "",
        "cmd_type": "ice",
        "request_type": "candidate",
        "candidate": "candidate:189685713 1 udp 2122260223 10.20.20.217 52128 "
                     "typ host generation 0 ufrag Gq2s network-id 1"
        }

#
# sdp += "v=0\r\n"
# sdp += "o=- 1631251864075308 1 IN IP4 " + GetLocalIP() + "\r\n"
# sdp += "s=-\r\n"
# sdp += "t=0 0\r\n"
# sdp += "a=group:BUNDLE audio video\r\n"
# sdp += "m=audio " + strconv.Itoa(localPort) + " RTP/AVP 8 111 0 103\r\n"
# sdp += "c=IN IP4 " + GetLocalIP() + "\r\n"
# sdp += "a=setup:active\r\n"
# sdp += "a=recvonly\r\n"
# sdp += "a=rtcp-mux\r\n"
# sdp += "a=rtpmap:8 PCMA/8000\r\n"
# sdp += "a=rtpmap:111 opus/48000/2\r\n"
# sdp += "a=rtcp-fb:111 transport-cc\r\n"
# sdp += "a=fmtp:111 minptime=10;useinbandfec=1;maxplaybackrate=16000\r\n"
# sdp += "a=rtpmap:103 mpeg4-generic/22050/1\r\n"
# sdp += "a=fmtp:103 streamtype=5;profile-level-id=1;mode=AAC-lbr;sizelength=13;indexlength=3;indexdeltalength=3;\r\n"
# sdp += "a=rtpmap:0 PCMU/8000\r\n"
# sdp += "m=video " + strconv.Itoa(localPort) + " RTP/AVP 96 102 116"
# sdp += "c=IN IP4 " + GetLocalIP() + "\r\n"
# sdp += "a=setup:active\r\n"
# sdp += "a=recvonly\r\n"
# sdp += "a=rtcp-mux\r\n"
# sdp += "a=rtpmap:96 H264/90000\r\n"
# sdp += "a=fmtp:96 level-asymmetry-allowed=1;packetization-mode=1\r\n"
# sdp += "a=rtcp-fb:96 nack\r\n"
# sdp += "a=rtcp-fb:96 nack pli\r\n"
# sdp += "a=rtpmap:102 HEVC/90000\r\n"
# sdp += "a=fmtp:102 packetization-mode=1\r\n"
# sdp += "a=rtcp-fb:102 nack\r\n"
# sdp += "a=rtcp-fb:102 nack pli\r\n"