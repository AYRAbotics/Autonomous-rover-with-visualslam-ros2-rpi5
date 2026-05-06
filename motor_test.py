from gpiozero import PWMOutputDevice, DigitalOutputDevice
from time import sleep

PWM_PIN = 18
DIR_PIN = 23

# Setup
pwm = PWMOutputDevice(PWM_PIN, frequency=1000)
direction = DigitalOutputDevice(DIR_PIN)

try:

    # Forward 50%
    print("Forward 50%")
    direction.on()
    pwm.value = 0.5
    sleep(5)

    # Forward 75%
    print("Forward 75%")
    pwm.value = 0.75
    sleep(5)

    # Stop briefly
    pwm.value = 0
    sleep(2)

    # Reverse 50%
    print("Reverse 50%")
    direction.off()
    pwm.value = 0.5
    sleep(5)

    # Reverse 75%
    print("Reverse 75%")
    pwm.value = 0.75
    sleep(5)

    # Stop
    print("Stopping")
    pwm.value = 0

finally:
    pwm.close()
    direction.close()
