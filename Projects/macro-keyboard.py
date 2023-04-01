import time
import digitalio
import board
import usb_hid
from adafruit_hid.Keyboard import Keyboard
from adafruit_hid.Keycode import Keycode



btn0_pin = board.GP15

keyboard = Keyboard(usb_hid.devices)

btn0 = digitalio.DigitalInOut(btn0_pin)
btn0_direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.UP

btn1_pin = board.GP14

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1_direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2_pin = board.GP13

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2_direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3_pin = board.GP12

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3_direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP



while True:
    if not btn0.value:
        print('button 0 pressed')
        keyboard.press(Keycode.ALT, Keycode.TAB)
        time.sleep(0.15)
        keyboard.release(Keycode.ALT, Keycode.TAB)
        
    if not btn1.value:
        print('button 1 pressed')
        keyboard.press(Keycode.GUI, Keycode.SEVEN)
        time.sleep(0.2)
        keyboard.release(Keycode.GUI, Keycode.SEVEN)
        
    if not btn2.value:
        print('button 2 pressed')
        keyboard.press(Keycode.CONTROL, Keycode.N)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.N)
        time.sleep(0.1)
        
        
    if not btn3.value:
        print('button 3 pressed')
        keyboard.press(Keycode.CONTROL, Keycode.W)
        time.sleep(0.2)
        keyboard.release(Keycode.CONTROL, Keycode.W)