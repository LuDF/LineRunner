import wiringpi
import time

# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
_max_speed = 480  # 19.2 MHz / 2 / 480 = 20 kHz
MAX_SPEED = _max_speed

io_initialized = False


def io_init():
    global io_initialized
    if io_initialized:
        return

    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(23, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pinMode(24, wiringpi.GPIO.PWM_OUTPUT)

    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    wiringpi.pwmSetRange(MAX_SPEED)
    wiringpi.pwmSetClock(2)

    wiringpi.pinMode(27, wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(22, wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(14, wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(15, wiringpi.GPIO.OUTPUT)

    io_initialized = True


class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin, dir_pin2):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin
        self.dir_pin2 = dir_pin2

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = 1
            dir_value2 = 0
        else:
            dir_value = 0
            dir_value2 = 1

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        io_init()
        wiringpi.digitalWrite(self.dir_pin, dir_value)
        wiringpi.digitalWrite(self.dir_pin2, dir_value2)
        wiringpi.pwmWrite(self.pwm_pin, speed)


class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(23, 27,14)
        self.motor2 = Motor(24, 22,15)

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)


motors = Motors()

test_forward_speeds = MAX_SPEED

try:
    motors.setSpeeds(0,0)
    print("Motor 2 forward")
    #for s in test_forward_speeds:
    motors.motor2.setSpeed(test_forward_speeds)
    time.sleep(10)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0,0)