from pythonosc import udp_client

class OSCCLient(object):
    def __init__(self, ip='127.0.0.1', port=9001):
        self.setup_client(ip, port)

    def setup_client(self, ip, port):
        self._client = udp_client.SimpleUDPClient(ip, port)

    def setAdress(self, ip, port):
        self.setup_client(ip, port)

    def send_message(self, index, value):
        self._client.send_message("/E", (int(index), float(value)*0.01))