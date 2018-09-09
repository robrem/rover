import board
import time
from adafruit_crickit import crickit
from digitalio import DigitalInOut, Direction, Pull

# Adjustment factors for motors at full speed
RIGHT_SPEED = 1.0
LEFT_SPEED = 0.9

button_A = DigitalInOut(board.BUTTON_A)
button_A.direction = Direction.INPUT
button_A.pull = Pull.DOWN
 
left_wheel = crickit.dc_motor_1
right_wheel = crickit.dc_motor_2
 
 
# These allow easy correction for motor speed variation.
# Factors are determined by observation and fiddling.
# Start with both having a factor of 1.0 (i.e. none) and
# adjust until the bot goes more or less straight
def set_right(speed):
    right_wheel.throttle = speed * 0.9
 
def set_left(speed):
    left_wheel.throttle = -speed
 
 
# Uncomment this to find the above factors
# set_right(1.0)
# set_left(1.0)
# while True:
#    pass
 
while True:
    if button_A.value:
        while True:
            # tack left
            set_left(0.25)
            set_right(RIGHT_SPEED)
            time.sleep(0.75)
         
            # tack right
            set_left(LEFT_SPEED)
            set_right(0.25)
            time.sleep(0.75)