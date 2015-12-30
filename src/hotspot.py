import subprocess

class Hotspot:
    """This contains methods that handle the intialization, starting and stopping of the hotspot"""

    def __init__(self, name = None, password = None):
        """initialize all the commands that are required"""
        self._initialize_cmd = "netsh wlan set hostednetwork mode = allow ssid = {} key = {}".format(name, password).split()
        self._start_cmd = "netsh wlan start hostednetwork".split()
        self._stop_cmd = "netsh wlan stop hostednetwork".split()

    def initialize_hotspot(self):
        """set the hostednetwork mode to allow and also the network name and password"""
        try:
            subprocess.check_call(self._initialize_cmd, shell=True)
        except subprocess.CalledProcessError as e:
            print("There was an issue starting the hotspot the wifi might be turned off from the hardware switch\nOr your network card is not compatible")

    def start(self):
        try:
            subprocess.check_call(self._start_cmd, shell=True)
            print("------------------------------------------")
            print("HOTSPOT successfully started")
        except subprocess.CalledProcessError as e:
            print("There was an issue starting the hotspot the wifi might be turned off from the hardware switch\nOr your network card is not compatible")

    def stop(self):
        try:
            subprocess.check_call(self._stop_cmd, shell=True)
            print("------------------------------------------")
            print("HOTSPOT has been stopped")
        except subprocess.CalledProcessError as e:
            print("No active wifi connection to stop")

if __name__ == "__main__": main()