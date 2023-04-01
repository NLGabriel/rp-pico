import time
import digitalio
import board
import usb_hid
from adafruit_hid.Keyboard import Keyboard
from adafruit_hid.Keycode import Keycode
from adafrui_hid.mouse import Mouse

btn1_pin = board.GP15 
#You can chose an other pin if you want

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3_direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

if not btn1.value:
        print('button 1 pressed')
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.01)
        #Chose the seconds between the clicks