import PicoRobotics
import utime
from machine import UART, Pin
board = PicoRobotics.KitronikPicoRobotics()
led = Pin(25, Pin.OUT)
led.toggle()
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
            print("highByte: ", highByte, "lowByte: ", lowByte)
            utime.sleep_ms(50)
    elif direction =="r":
        print("CounterClockwise Turn (backward)")
        for lowByte in range(60,150):
            #PWMVal = int((degrees*2.2755)+102) #
            #lowByte = PWMVal & 0xFF
            highByte = 1
            board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo,bytes([lowByte]))
            board.i2c.writeto_mem(board.CHIP_ADDRESS, calcServo+1,bytes([highByte]))
            print("highByte: ", highByte, "lowByte: ", lowByte)
            utime.sleep_ms(50)


testServo(board,1,"f")
testServo(board,1,"r")
stopServo(board,1)
    
