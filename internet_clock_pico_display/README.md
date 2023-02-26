# Raspberry Pi Pico W with Pico Display Real Time Clock

A Digital Clock that uses WIFI to set the time. A Good example of using both Pico W and Pico Display.

---
<p align="center">
<img src="https://user-images.githubusercontent.com/32769732/221332031-8d5de5b9-74e3-417f-8893-0f67f1277c0e.png"  width="600" height="600">
  <p/>
  
Out of 4 buttons 2 of them utilized. The X and Y buttons are used for setting the brigthness of the clock. The A and B buttons and the RGB LED can be used for other things, sending a ping etc.
  
 ## How to use:
 
1) Insert your Network name and password:
```
# Wifi Settings
ssid = ''
password = ''
```
2) If needed add your own timezone to the code:
```
def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA    
    tm = time.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], [6] + <YOUR_TIME_ZONE>, tm[3], tm[4], tm[5], 0))
 ```
  3) upload the `main.py` and it is ready to use!
  
  ## TODO
  Instead of looping a while loop and waiting for button calls come up with a more energy efficient idea. 
  
  Here is an inspiration: https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/
