# Resetting Flash memory
Pico’s BOOTSEL mode lives in read-only memory inside the RP2040 chip, and can’t be overwritten accidentally. No matter what, if you hold down the BOOTSEL button when you plug in your Pico, it will appear as a drive onto which you can drag a new UF2 file. There is no way to brick the board through software. However, there are some circumstances where you might want to make sure your Flash memory is empty. You can do this by dragging and dropping a special UF2 binary onto your Pico when it is in mass storage mode.

1)  a)Download the UF2 file from here: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html

    b) or use "flash_nuke.uf2" file from this folder

2)  Go to Thonny on the most bottom right select Micropython(Raspberry Pi Pico), and install the MicroPython

3) Stop/Restart the editor in Thonny, you will see something like this: 

"""MicroPython v1.18 on 2022-01-17; Raspberry Pi Pico with RP2040

Type "help()" for more information."""