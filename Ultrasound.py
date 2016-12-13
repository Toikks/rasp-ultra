def trig_Sensor(Pin):               #Keep output pin true for 10uS
    GPIO.output(Pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Pin, GPIO.LOW)
    return

def echo_Sensor(Pin):               #Count how long input is true in [uS].
    pulse_end = pulse_start = 0
    while GPIO.input(Pin) == 0:
        pulse_start = time.time()
    while GPIO.input(Pin) == 1:
        pulse_end = time.time()
    return pulse_end - pulse_start

def measure_Distance():             #Calculate distance from sound traveltime
    trig_Sensor(outPin)
    return echo_Sensor(inPin) * 340.29 / 2


if __name__ == '__main__':
    import Rpi.GPIO as GPIO
    import time

    inPin = 23  # Echo from sensor
    outPin = 24  # Sensor trigger

    GPIO.setmode(GPIO.BOARD)  # Setting up pins
    GPIO.setup(inPin, GPIO.IN)  # echo
    GPIO.setup(outPin, GPIO.OUT)  # trigger

    print(measure_Distance())