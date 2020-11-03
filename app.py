from sinric import Sinric
from wakeonlan import send_magic_packet

apiKey = 'YourApiKey'  # https://sinric.com
pc_mac = 'aa:bb:cc:dd:ee:ff' # The interface mac address of the pc
device_id = "YourDeviceId" # Grab it from https://sinric.com too


def power_state(deviceId, state):
    if deviceId == device_id and state == 'ON':
        send_magic_packet(pc_mac)



if __name__ == "__main__":
    callbacks = {"setPowerState": power_state}    
    app = Sinric(apiKey, callbacks)
    print("Alexa wake on lan started...")
    app.handle()
    
