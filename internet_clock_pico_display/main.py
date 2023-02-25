#WIRELESS RELATED
import network
import socket
from time import sleep
import machine
import struct

#DISPLAY RELATED
import time
from pimoroni import Button,RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4


#WIFI settings
led = machine.Pin("LED", machine.Pin.OUT)
led.off()
led = RGBLED(6, 7, 8)
led.set_rgb(0, 0, 0)

ssid = 'Michelangelo'
password = 'MyB1gDav1d'

# We're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)
back_light = 0.5
display.set_backlight(back_light)
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)

w, h = display.get_bounds()


### Display related    
# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

def change_backlight(display,amount=0.1):
    global back_light
    back_light = round(back_light + amount,2)
    if back_light >=1.0:
        back_light = 1.0
    elif back_light  <= 0.1:
        back_light = 0.1
        
    display.set_backlight(back_light)
    
#WIFI Connection

NTP_DELTA = 2208988800
host = "pool.ntp.org"

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
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
   
def update_time():
    is_updated = False
    while is_updated == False:
        try:
            #led.on()
            set_time()
            is_updated = True
            print("time is updated")
            #led.off()
        except OSError as exc:
            if exc.args[0] == 110: #ETIMEDOUT
                time.sleep(2)
                pass
            
def get_time():
    year, month, day, GMT, hours, minutes, seconds, _ = machine.RTC().datetime()
    year = str(year)
    month =str(month)
    day = str(day)
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    
    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day      
    if len(hours) < 2:
        hours = "0" + hours      
    if len(minutes) < 2:
        minutes = "0" + minutes       
    if len(seconds) < 2:
        seconds = "0" + seconds
    
    day_time = f"{hours}:{minutes}"
    date = f"{day}/{month}/{year}"
    
    return day_time, date
    
def update_clock_display():
    clear()
    day_time,date = get_time()
    display.set_pen(YELLOW)
    display.text(day_time,int(w/4), int(h/4), 240, 8)            
    display.text(date,int(w/4), int(6*h/8), 240, 3)          
    display.update()
    
    return day_time,date 

#################################################################
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    clear()
    display.set_pen(YELLOW)
    display.text("waiting for connection...",int(w/4), int(h/4), 240, 3)
    display.update()
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    clear()
    display.set_pen(YELLOW)
    display.text("connected",int(w/4), int(h/4), 240, 3)
    display.update()
    print('connected')
    time.sleep(1)
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
# set up
update_time()
old_day_time, old_date = update_clock_display()
day_time = old_day_time
date = old_date


while True:
    if button_a.read():                                   # if a button press is detected then...
        clear()                                           # clear to black
        display.set_pen(WHITE)                            # change the pen colour
        display.text("Hello", int(w/4), int(h/4), 240, 3)  # display some text on the screen
        display.update()                                  # update the display
        time.sleep(1)                                     # pause for a sec
        update_clock_display()                                         # clear to black again
    elif button_b.read():
        clear()
        display.set_pen(CYAN)
        display.text("Basma", int(w/6), int(h/4), 240, 8)
        display.update()
        time.sleep(1)
        update_clock_display()
    elif button_x.read():
        clear()
        display.set_pen(MAGENTA)
        change_backlight(display,amount=0.1)
        display.text(f"{back_light}",int(w/4), int(h/4), 240, 4)
        display.update()
        time.sleep(0.2)
        update_clock_display()
    elif button_y.read():
        clear()
        display.set_pen(GREEN)        
        change_backlight(display,amount= -0.1)
        display.text(f"{back_light}",int(w/4), int(h/4), 240, 4)
        display.update()
        time.sleep(0.2)
        update_clock_display()
    else:
        day_time, date = get_time()
        if day_time != old_day_time:
             old_day_time, old_date = update_clock_display()
        
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses

        





