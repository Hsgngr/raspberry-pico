from machine import Pin, PWM
from utime import sleep

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
    
def bequiet():
    buzzer.duty_u16(0)
    
def playsong(mysong,length=0.1):
    for i in range(len(mysong)):
        if mysong[i] < 31:
            buzzer.freq(31)
            buzzer.duty_u16(0)
        else:
            playtone(mysong[i])
        sleep(length)
    bequiet()


buzzer = PWM(Pin(18))
#Copy paste your tone.txt
song = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2638, 2635, 2637, 2640, 2641, 2638, 2636, 2636, 2638, 2640, 1179, 1176, 1175, 1175, 1176, 1176, 1175, 1175, 1176, 1176, 1175, 1175, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 832, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 0, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 0, 988, 988, 988, 988, 988, 988, 988, 989, 988, 988, 988, 0, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 0, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 0, 988, 988, 988, 988, 988, 988, 988, 988, 988, 988, 988, 0, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 0, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 0, 0, 0, 2650, 5268, 5257, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2633, 2635, 2635, 2639, 2640, 2639, 2637, 2635, 2637, 2639, 2640, 2638, 0, 1175, 1175, 1175, 1175, 1175, 1175, 1175, 1175, 1175, 1175, 1175, 0, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 740, 0, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 831, 0, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 1109, 0, 988, 989, 988, 988, 988, 988, 988, 988, 988, 988, 988, 0, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 587, 660, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 988, 988, 988, 988, 988, 988, 988, 988, 988, 988, 988, 990, 881, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 879, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 554, 555, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 659, 882, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 880, 0, 2675, 0, 2655, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

playsong(song,0.01)
buzzer.duty_u16(0)

