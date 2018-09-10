import random
import time
from adafruit_circuitplayground.express import cpx
from adafruit_crickit import crickit

LEFT = False
RIGHT = True

# Adjustment factors for motors at full speed
RIGHT_SPEED = 1.0
LEFT_SPEED = 0.9

SHAKE_THRESHOLD = 10
 
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

# React to accelerameter shake (bumped into something)
# and try to move away.
# Returns True if we're clear, False otherwise.
def react_to_shake():
    print("We are shaking!")
    set_right(0.0)
    set_left(0.0)
    attempts = 0

    while True:
        if attempts == 3:
            return False

        if not cpx.shake(shake_threshold=SHAKE_THRESHOLD):
            return True

        # Back up
        set_right(-0.5)
        set_left(-0.5)
        time.sleep(1.0)

        # Try turning right
        set_right(0.25)
        set_left(LEFT_SPEED)

        # Turn for this amount of time
        time.sleep(random.choice([0.3, 0.4, 0.5]))
        attempts += 1


# Move in direction for duration. Returns True if move is 
# successful, False otherwise.
def tack(direction, duration):
    target_time = time.monotonic() + duration

    if direction == LEFT:
        set_left(0.25)
        set_right(RIGHT_SPEED)
    else:
        set_left(LEFT_SPEED)
        set_right(0.25)

    while time.monotonic() < target_time:
        if cpx.shake(shake_threshold=SHAKE_THRESHOLD):
            return react_to_shake()

    return True
 
 
# Uncomment this to find the above factors
# set_right(1.0)
# set_left(1.0)
# while True:
#    pass
 
while True:
    if not tack(LEFT, 0.75):
        break
    if not tack(RIGHT, 0.75):
        break

set_right(0.0)
set_left(0.0)