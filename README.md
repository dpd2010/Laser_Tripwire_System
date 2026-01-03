# alarm_system

# Raspberry Pi Pico Laser Tripwire Alarm

A simple laser tripwire system using a Raspberry Pi Pico, a photoresistor module, and an active buzzer.  
When the laser beam is broken, the buzzer sounds an alarm. This project is great for learning about MicroPython, ADC readings, and basic electronics.

---

## Components Needed

- Raspberry Pi Pico (or Pico W)
- Active buzzer module
- Laser module
- Phototransistor or LDR (light sensor) module
- Jumper wires
- Breadboard
- 3.3V power supply (USB or power bank)

---

## Wiring

- **Laser module:** connect VCC to 3.3V, GND to GND, aim at the sensor
- **Light sensor (LDR or phototransistor):**  
  - VCC to 3.3V  
  - GND to GND  
  - Signal to ADC pin GP26
- **Buzzer:**  
  - Positive pin to GP15  
  - Negative pin to GND

---

## Setup

1. Install MicroPython on your Pico: [https://www.raspberrypi.com/documentation/microcontrollers/micropython.html](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
2. Copy the code (`main.py`) to your Pico using Thonny IDE or rshell.
3. Make sure your laser is aligned with the sensor.

---

## Usage

1. Power the Pico.
2. The laser hits the sensor.
3. When the beam is broken, the buzzer will beep.

---

## Calibration

- Adjust the `THRESHOLD` in the code according to your environment’s light conditions.
- Test different positions and distances to ensure reliable triggering.

---

## Future Improvements

- Add an OLED display to show status (“ARMED” / “TRIGGERED”)
- Connect Pico W to send notifications over Wi-Fi
- Use a passive buzzer to play a siren pattern

