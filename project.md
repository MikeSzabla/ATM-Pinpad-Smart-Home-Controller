# PROJECT.md

# ATM Pinpad Home Assistant Control Surface

## Overview

This project repurposes a reclaimed ATM PIN pad into a programmable Home Assistant control surface using an ESP32 running MicroPython.

Unlike a traditional remote control, this device is intended to function as a dedicated interface into my personal Home Assistant ecosystem. The keypad provides physical input while an OLED display presents a navigable UI driven entirely by Home Assistant.

This project is intended for personal use only. While the architecture is designed to be expandable and maintainable, there are no plans to package or distribute the firmware.

---

# Project Goals

## Primary Goals

- Reuse authentic ATM hardware.
- Learn embedded development with ESP32 and MicroPython.
- Build a responsive physical interface for Home Assistant.
- Design firmware that is modular and easy to extend.
- Separate hardware control from application logic.

## Non Goals

- Commercial release
- Generic firmware for arbitrary ATM keypads
- Direct Home Assistant API integration
- Cloud connectivity

---

# Current Hardware

## Controller

ESP32 running MicroPython

## Input Device

Reclaimed ATM keypad

Current reverse engineering indicates:

- One dedicated trace per button
- Shared common connection
- Configured as active-low inputs using ESP32 internal pull-up resistors

Current proof of concept has validated:

- Common connected to ESP32 GND
- Individual button connected to GPIO
- Successful button detection

## Display

0.96" GME12864 OLED

Controller:
SSD1306

Interface:
I²C

The display abstraction should allow replacement with another display in the future without requiring significant application changes.

---

# Software Architecture

The project intentionally follows a separation-of-responsibilities architecture.

```
boot.py
    Low-level initialization

main.py
    Application entry point
    Coordinates all modules

config.py
    Non-secret project configuration

secrets.py
    WiFi / MQTT credentials

logger.py
    Logging abstraction

wifi.py
    WiFi management

mqtt_client.py
    MQTT connectivity

keypad.py
    Keypad hardware interface

display.py
    OLED hardware driver

ui.py (future)
    Screen rendering

state.py (future)
    Shared application state
```

Each module owns exactly one responsibility.

---

# Design Principles

The project favors:

- Readability over cleverness
- Small focused modules
- Object-oriented abstractions where appropriate
- Low coupling
- High cohesion
- Hardware abstraction
- Easy future expansion

Avoid:

- Global state
- Large "god" classes
- Hardware-specific logic scattered throughout the project

---

# System Architecture

```
ATM Keypad
        │
        ▼
ESP32 Firmware
        │
────────┼────────
        │
 WiFi Manager
 MQTT Manager
 Display
 Keypad
 UI
        │
        ▼
 Mosquitto
        │
        ▼
Home Assistant
```

Home Assistant is considered the system of record.

The ESP32 is a terminal.

---

# MQTT Philosophy

MQTT is the only communication layer between the ESP32 and Home Assistant.

The ESP32 should never communicate directly with Home Assistant's REST or WebSocket APIs.

Instead:

Home Assistant publishes state.

ESP32 publishes user input.

---

# MQTT Discovery

The device will integrate with Home Assistant using MQTT Discovery.

Advantages:

- Automatic device registration
- Native Home Assistant device representation
- Device triggers
- Reduced manual configuration

---

# UI Philosophy

The OLED is not a diagnostic display.

It is the primary user interface.

Diagnostics are secondary.

The display should present information naturally navigated using the ATM keypad.

---

# UI Navigation

Initial screen:

```
Select Room

> Kitchen

  Living Room

  Bedroom

  Office
```

Rooms are dynamically provided by Home Assistant.

Selecting a room loads the available controllable entities.

Example:

```
Kitchen

> Island Lights

  Sink Lights

  Ceiling Fan

  Coffee Outlet
```

Each list is dynamically generated.

The ESP32 should never hardcode rooms or entities.

---

# Entity Control Screen

Selecting an entity displays:

```
Kitchen Lights

Brightness

██████░░░░ 60%
```

Controls:

Left
-10%

Right
+10%

Numeric Keys

Enter exact brightness percentage.

Example:

```
7
5
Enter

→ 75%
```

Buttons:

Enter
Apply entered value

Cancel
Back

Clear
Clear current numeric input

---

# Ownership of State

Home Assistant owns:

- Rooms
- Entity names
- Brightness
- Availability
- Device state

ESP32 owns:

- Current screen
- Cursor position
- Temporary numeric input
- Navigation history

If Home Assistant changes state, the ESP32 updates its display.

---

# Current Status

Completed

✓ Reverse engineered keypad

✓ GPIO input proof of concept

✓ WiFi connectivity

✓ MQTT connectivity

✓ MQTT publishing

✓ Home Assistant communication

✓ Modular firmware architecture

In Progress

• OLED integration

Planned

• MQTT subscriptions

• Display manager

• UI framework

• MQTT Discovery

• Remaining keypad wiring

---

# Future Roadmap

Phase 1
Hardware validation
✓ Complete

Phase 2
Networking
✓ Complete

Phase 3
MQTT communication
✓ Complete

Phase 4
OLED integration

Phase 5
Home Assistant Discovery

Phase 6
Navigation framework

Phase 7
Dynamic room/entity synchronization

Phase 8
Entity control

Phase 9
Animations and UI polish

---

# Long-Term Vision

The finished project should feel less like an ESP32 development board and more like a purpose-built Home Assistant appliance.

The user should be able to:

- Wake the device
- Browse rooms
- Browse devices
- Control brightness
- Toggle switches
- Receive immediate visual feedback

without ever needing to know that MQTT or Home Assistant are operating behind the scenes.

The firmware should remain modular enough that new hardware (additional displays, LEDs, buzzers, card readers, etc.) can be incorporated without requiring major architectural changes.

---

# Guiding Principle

Home Assistant is the brain.

The ESP32 is the hands and eyes.

The firmware should focus on presenting a responsive, intuitive physical interface while Home Assistant remains responsible for application logic, automation, and state management.