# Laser Tripwire Alarm (Raspberry Pi Pico)

A portable laser tripwire alarm built using a **Raspberry Pi Pico**, an **LDR**, and an **active buzzer**. When the laser beam is interrupted, the buzzer immediately sounds for **5 seconds**, even if the laser is restored sooner. The project combines simple electronics, analogue sensing, and MicroPython, and is designed to be reliable enough to leave running for long periods.

This README is written so that someone with basic electronics knowledge could **rebuild the entire project from scratch**, both hardware and software.

---

## Project Overview

* A laser pointer is aimed at an LDR housed in a small tube (straw) to block ambient light
* The LDR is part of a voltage divider connected to an ADC pin on the Pico
* The Pico continuously monitors the light level
* When the laser beam is broken, the buzzer immediately sounds
* Once triggered, the buzzer **always stays on for a full 5 seconds**, even if the beam is restored
* After 5 seconds, the system resets and is ready for the next trigger

The entire system is battery powered and housed in a small portable enclosure.

---

## Hardware Required

* Raspberry Pi Pico (or Pico 2 W)
* Active buzzer (3.3 V compatible)
* LDR (Light Dependent Resistor)
* 10 kΩ resistor (for voltage divider)
* Laser pointer (standalone, battery powered – not connected electrically)
* Breadboard
* Jumper wires (male–male)
* USB battery pack (or wall USB charger)
* USB cable for Pico

### Optional / Recommended

* LED + 220 Ω resistor (used as a power indicator / power-bank keep-alive load)
* Black straw or tube (for shielding the LDR)
* Electrical tape or heat-shrink tubing
* Small project enclosure / box

---

## How the Circuit Works

The Pico cannot measure resistance directly, so the LDR is used in a **voltage divider** configuration:

* Bright light (laser on LDR) → LDR resistance decreases → ADC voltage increases
* Laser blocked → LDR resistance increases → ADC voltage decreases

The Pico reads this voltage using one of its ADC pins and compares it to a threshold.

---

## Wiring Instructions

### LDR Voltage Divider

```
3V3_OUT ── LDR ──┬── GP26 (ADC0)
                  |
                10 kΩ
                  |
                 GND
```

Important notes:

* Use **3V3_OUT**, not 3V3_EN
* GP26 must be connected to the **junction** between the LDR and the resistor
* Only GP26, GP27, and GP28 are ADC-capable pins

### Buzzer Wiring (Active Buzzer)

```
Buzzer +  → GP17
Buzzer −  → GND
```

No PWM is required because the buzzer is active.

### Power

* The Pico is powered via USB from a battery pack or wall charger
* All components are powered from the Pico’s 3.3 V rail

---

## Software Setup

### Requirements

* MicroPython installed on the Raspberry Pi Pico
* Code uploaded using Thonny or a similar editor( i used vscode and used pico extension)

## Choosing the Threshold Value

To find a good threshold:

1. Run a simple test program that prints `ldr.read_u16()`
2. Note the value when the laser is directly on the LDR
3. Note the value when the laser is blocked
4. Set `THRESHOLD` roughly halfway between the two values

This makes the system resistant to changes in room lighting.

---

## Housing and Physical Assembly

To make the system portable and reliable:

* The Pico, breadboard, buzzer, and wiring were placed inside a **small portable box**
* The LDR was mounted so it pokes out of the box through a **black straw**, acting as a light tunnel
* The straw dramatically reduces interference from ambient room light
* The battery pack was taped to the back of the box
* The laser pointer was placed separately, aimed directly at the LDR straw opening

This setup allows the entire system to be repositioned easily without rewiring.

---

## Problems Encountered and How They Were Fixed

### 1. ADC Values Not Changing

**Problem:** The ADC reading stayed around 12,000–14,000 regardless of light level.

**Cause:** The ADC pin was floating due to incorrect wiring and incorrect pin identification.

**Fix:**

* Verified the correct ADC-capable pin (GP26)
* Ensured the LDR and resistor shared the same junction
* Confirmed connections using direct GP26 → GND and GP26 → 3V3 tests

---

### 2. Very Small Change Between Laser On / Off

**Problem:** The laser made little difference to the ADC readings.

**Cause:** Ambient room light dominated the LDR.

**Fix:**

* Shielded the LDR using a black straw
* Carefully aligned the laser with the straw

---

### 3. Buzzer Not Ringing for Full 5 Seconds

**Problem:** The buzzer stopped early if the laser was restored.

**Cause:** Timer logic was being reset by changes in the laser state.

**Fix:**

* Used `time.ticks_ms()` and a state variable to ensure the timer runs independently of the laser after triggering

---

### 4. System Stopping After a Few Minutes

**Problem:** After being left idle, the system appeared to stop working.

**Cause:** The USB power bank automatically shut off due to low current draw.

**Fix:**

* can switch power supply to a wall charger 
* Added a small constant load (LED + resistor) to keep the power bank awake
* i personally just left it be because i wanted my projct to be portable as it was a main requirement

---

## What This Project Demonstrates

* Analogue sensing using ADCs
* Voltage divider design
* Real-world debugging of hardware and software
* Timing logic on microcontrollers
* Power management considerations in embedded systems
* Practical enclosure design for reliability

---

## Possible Extensions

* Add Wi-Fi alerts (Pico W)
* Log trigger events
* Add an arming switch if laser tripwire set off (trigger nerf gun?)

---

## License

This project is open for learning and personal use. Feel free to adapt or extend it.
