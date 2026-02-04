from machine import Pin, ADC
import time

ldr = ADC(26)          # GP26 / ADC0
buzzer = Pin(17, Pin.OUT)

THRESHOLD = 50000      # Adjust based on your LDR readings
BUZZ_TIME = 5000       # milliseconds (5 seconds)

buzzing = False        # Tracks if buzzer is currently buzzing
buzz_start = 0         # Stores when the buzzer started

while True:
    value = ldr.read_u16()
    laser_blocked = value < THRESHOLD
    now = time.ticks_ms()

    if laser_blocked and not buzzing:
        # Laser just got blocked → start buzzing
        buzzing = True
        buzz_start = now
        buzzer.on()

    # If buzzing, check if 5 seconds have passed
    if buzzing:
        if time.ticks_diff(now, buzz_start) >= BUZZ_TIME:
            buzzer.off()
            buzzing = False

    time.sleep(0.05)
