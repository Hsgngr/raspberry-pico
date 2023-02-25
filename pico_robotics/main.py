import pico_ble
import PicoRobotics
import utime
import time
from machine import UART, Pin
board = PicoRobotics.KitronikPicoRobotics()
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))


pico_ble.Pico_BLE_init()


def stopServo(board,servo):
    
    highByte= 0
    lowByte = 0
    calcServo = board.SRV_REG_BASE + ((servo - 1) * board.REG_OFFSET)
    board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo,bytes([highByte]))
    board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo+1,bytes([lowByte]))


def testServo(board,servo,direction):
    calcServo = board.SRV_REG_BASE + ((servo - 1) * board.REG_OFFSET)
    if direction == "f":
        print("Clockwise Turn (forward)")
        for degrees in range(90,0,-1):
            #PWMVal = int((degrees*2.2755)+102) #
            PWMVal = int((degrees*2.2755)+102) # see comment above for maths
            lowByte = PWMVal & 0xFF
            highByte = (PWMVal>>8)&0x01
            
            board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo,bytes([lowByte]))
            board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo+1,bytes([highByte]))
            #print("highByte: ", highByte, "lowByte: ", lowByte)
            utime.sleep_ms(1)
    elif direction =="r":
        print("CounterClockwise Turn (rear)")
        for lowByte in range(60,150):
            #PWMVal = int((degrees*2.2755)+102) #
            #lowByte = PWMVal & 0xFF
            highByte = 1
            board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo,bytes([lowByte]))
            board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo+1,bytes([highByte]))
            #print("highByte: ", highByte, "lowByte: ", lowByte)
            utime.sleep_ms(1)

    
    

while True:
    led = Pin(25, Pin.OUT)
    led.toggle()
    time.sleep_ms(20)
    if uart.any() > 0:
        rxData = uart.read()
#         time.sleep_ms(20)
        print(rxData)
        data = (rxData.decode("utf-8")).replace("\n","") #Convert to readable format (byte to string)
        
        if "right" == data:
            uart.write(rxData)           
            for degrees in range(30,60,1):
                board.servoWrite(1,degrees)
                utime.sleep_ms(10)
            
        elif "left" == data:
            uart.write(rxData)
            for degrees in range(60,30,-1):
                board.servoWrite(2,degrees)
                utime.sleep_ms(10)
                
        elif "both" == data:
            uart.write(rxData)
            for degrees in range(30,60,1):
                board.servoWrite(1,degrees)
                board.servoWrite(2,90-degrees)
                utime.sleep_ms(10)
                
            
        elif "stop" == data:
            uart.write(rxData)
            for servo in range(1,8):
                stopServo(board,1)
                
        elif "open_lid" == data:
            uart.write(rxData)
            for degrees in range(0,90):
                board.servoWrite(3,60)
                board.servoWrite(4,120)
                utime.sleep_ms(1)
        
        elif "close_lid" == data:
            uart.write(rxData)
            for degrees in range(0,90):
                board.servoWrite(3,120)
                board.servoWrite(4,60)
                utime.sleep_ms(1)
                
        
        elif "wait_and_open" == data:
            utime.sleep_ms(5000)
            uart.write(rxData)
            for degrees in range(0,90):
                board.servoWrite(3,60)
                board.servoWrite(4,120)
                utime.sleep_ms(1)
                
            utime.sleep_ms(2000)
            uart.write(rxData)
            for degrees in range(0,90):
                board.servoWrite(3,120)
                board.servoWrite(4,60)
                utime.sleep_ms(1)

        
    



