#####Buttons for Pokemon #########
##### 04/28/21
################################
import RPi.GPIO as GPIO
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Buttons #
selectButton = 18
leftButton = 19
downButton = 20
rightButton = 21
upButton = 22

# Setups #
GPIO.setmode(GPIO.BCM)
GPIO.setup(selectButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leftButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(downButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(upButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# buttons #

# A button #
def select(channel):
    print('A button was pressed')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# directional buttons #
def left(channel):
    keyboard.press(Key.left)
    keyboard.release(Key.left)


def down(channel):
    keyboard.press(Key.down)
    keyboard.release(Key.down)


def right(channel):
    keyboard.press(Key.right)
    keyboard.release(Key.righ)


def up(channel):
    keyboard.press(Key.up)
    keyboard.release(Key.up)


# When the A button is pressed, simulates enter
GPIO.add_event_detect(selectButton, GPIO.FALLING, callback=select, bouncetime=300)

# When the left button is pressed, simulates left arrow
GPIO.add_event_detect(leftButton, GPIO.FALLING, callback=left, bouncetime=300)

# When the down button is pressed, simulates down arrow
GPIO.add_event_detect(downButton, GPIO.FALLING, callback=down, bouncetime=300)

# When the right button is pressed, simulates right arrow
GPIO.add_event_detect(rightButton, GPIO.FALLING, callback=right, bouncetime=300)

# When the up button is pressed, simulates up arrow
GPIO.add_event_detect(upButton, GPIO.FALLING, callback=up, bouncetime=300)

try:
    while True:
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()