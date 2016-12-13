# Used for Raspberry pi 3 model B with HC-SR04 ultrasound sensor.
# This program will find distance from the sensors sonic pulse echoing time and output it to a file.


def trig_sensor(pin):               # Keep output pin true for 10uS
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(pin, GPIO.LOW)
    return


def echo_sensor(pin):               # Count how long input is true in [uS].
    pulse_end = pulse_start = 0
    while GPIO.input(pin) == 0:
        pulse_start = time.time()
    while GPIO.input(pin) == 1:
        pulse_end = time.time()
    return pulse_end - pulse_start


def measure_distance():             # Calculate distance from sound traveltime
    trig_sensor(outPin)
    return echo_sensor(inPin) * 340.29 / 2


def writefile(distance):                # Writes distance as tring to a file 'distance.txt' for later use
    with open('distance.txt', 'w') as open_file:
        open_file.write(str(distance) + ' m')
        open_file.close()
        return


if __name__ == '__main__':
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)          # Setting up pins
    GPIO.setup(23, GPIO.IN)         # Echo from sensor in 23
    GPIO.setup(24, GPIO.OUT)        # Trigger to sensor in 24
    inPin = 23
    outPin = 24

    writefile(measure_distance())
