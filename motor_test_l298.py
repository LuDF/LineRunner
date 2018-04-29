from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

# ///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 23  # ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 27  # IN1 - Forward Drive
REVERSE_LEFT_PIN = 5  # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 24  # ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 22  # IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6  # IN2 - Reverse Drive

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)


def allStop():
    forwardLeft.value = False
    reverseLeft.value = False
    forwardRight.value = False
    reverseRight.value = False
    driveLeft.value = 0
    driveRight.value = 0


def forwardDrive():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 1.0
    driveRight.value = 1.0


def reverseDrive():
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = 1.0
    driveRight.value = 1.0


def spinLeft():
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 1.0
    driveRight.value = 1.0


def SpinRight():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = 1.0
    driveRight.value = 1.0


def forwardTurnLeft():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 0.2
    driveRight.value = 0.8


def forwardTurnRight():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 0.8
    driveRight.value = 0.2


def main():
    print("Starting")
    allStop()
    forwardDrive()
    print("Step")
    sleep(2)
    reverseDrive()
    print("Step")
    sleep(2)
    spinLeft()
    print("Step")
    sleep(2)
    SpinRight()
    print("Step")
    sleep(2)
    forwardTurnLeft()
    print("Step")
    sleep(2)
    forwardTurnRight()
    print("Step")
    sleep(2)
    allStop()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()