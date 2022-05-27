import time
from neopixel import Neopixel
 
numpix = 1
pixel = Neopixel(numpix, 0, 28, "GRB")
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color0 = red
 
pixel.brightness(100)
pixel.set_pixel(0, blue)
pixel.show()


while True:
    if color0 == red:
       color0 = blue
    else:
        color0 = red
        
    pixel.set_pixel(0,color0)
    pixel.show()
    time.sleep(0.1)