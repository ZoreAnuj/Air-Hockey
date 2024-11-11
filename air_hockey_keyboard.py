# # import serial
# # import time
# # from pynput import keyboard

# # # Replace with your Arduino port
# # arduino_port = "COM3"  # For Windows
# # # arduino_port = "/dev/ttyUSB0"  # For Linux/Mac

# # baud_rate = 9600  # Match the baud rate with the Arduino code
# # timeout = 1  # Timeout for serial communication

# # # Establish the serial connection
# # ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
# # time.sleep(2)  # Give time for the connection to establish

# # def send_command(command):
# #     """Send a single character command to Arduino."""
# #     if ser.is_open:
# #         ser.write(command.encode())
# #         print(f"Sent command: {command}")
# #         time.sleep(0.05)  # Small delay for Arduino to process the command

# # def on_press(key):
# #     """Handle key press events and send corresponding commands to Arduino."""
# #     try:
# #         if key.char == 'w':  # Move forward
# #             send_command('F')
# #         elif key.char == 'a':  # Move left
# #             send_command('L')
# #         elif key.char == 's':  # Move backward
# #             send_command('B')
# #         elif key.char == 'd':  # Move right
# #             send_command('R')
# #     except AttributeError:
# #         # Handle special keys (e.g., arrow keys) if needed
# #         pass

# # def on_release(key):
# #     """Stop sending commands when keys are released."""
# #     if key == keyboard.Key.esc:  # Stop if Esc key is pressed
# #         return False

# # # Start listening to keyboard events
# # listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# # listener.start()

# # print("Control the Arduino with your keyboard (WASD). Press ESC to exit.")

# # # Keep the script running and control continuous communication
# # try:
# #     listener.join()  # Keep the program alive and listening for keyboard inputs
# # except KeyboardInterrupt:
# #     print("Program interrupted.")
# # finally:
# #     if ser.is_open:
# #         ser.close()
# #         print("Serial connection closed")


# import serial
# import time
# from pynput import keyboard

# # Replace with your Arduino port
# arduino_port = "COM3"  # For Windows
# # arduino_port = "/dev/ttyUSB0"  # For Linux/Mac

# baud_rate = 9600  # Match the baud rate with the Arduino code
# timeout = 1  # Timeout for serial communication

# # Establish the serial connection
# ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
# time.sleep(2)  # Give time for the connection to establish

# def send_command(command):
#     """Send a single character command to Arduino."""
#     if ser.is_open:
#         ser.write(command.encode())
#         print(f"Sent command: {command}")
#         time.sleep(0.05)  # Small delay for Arduino to process the command

# def attack():
#     """Send two forward steps for the attack action."""
#     print("Attack: Moving forward for 2 steps")
#     for _ in range(2):  # Move forward for 2 steps
#         send_command('F')
#         time.sleep(0.1)  # Small delay between steps

# def on_press(key):
#     """Handle key press events and send corresponding commands to Arduino."""
#     try:
#         if key.char == 'w':  # Move forward
#             send_command('F')
#         elif key.char == 'a':  # Move left
#             send_command('L')
#         elif key.char == 's':  # Move backward
#             send_command('B')
#         elif key.char == 'd':  # Move right
#             send_command('R')
#     except AttributeError:
#         # Handle special keys (e.g., spacebar for attack)
#         if key == keyboard.Key.space:
#             attack()  # Perform attack action

# def on_release(key):
#     """Stop sending commands when keys are released."""
#     if key == keyboard.Key.esc:  # Stop if Esc key is pressed
#         return False

# # Start listening to keyboard events
# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()

# print("Control the Arduino with your keyboard (WASD for movement, Spacebar for attack). Press ESC to exit.")

# # Keep the script running and control continuous communication
# try:
#     listener.join()  # Keep the program alive and listening for keyboard inputs
# except KeyboardInterrupt:
#     print("Program interrupted.")
# finally:
#     if ser.is_open:
#         ser.close()
#         print("Serial connection closed")

import serial
import time
from pynput import keyboard

# Replace with your Arduino port
arduino_port = "COM3"  # For Windows
# arduino_port = "/dev/ttyUSB0"  # For Linux/Mac

baud_rate = 9600  # Match the baud rate with the Arduino code
timeout = 1  # Timeout for serial communication

# Establish the serial connection
ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
time.sleep(2)  # Give time for the connection to establish

def send_command(command):
    """Send a single character command to Arduino."""
    if ser.is_open:
        ser.write(command.encode())
        print(f"Sent command: {command}")
        time.sleep(0.05)  # Small delay for Arduino to process the command

def on_press(key):
    """Handle key press events and send corresponding commands to Arduino."""
    try:
        if key.char == 'w':  # Move forward
            send_command('F')
        elif key.char == 'a':  # Move left
            send_command('L')
        elif key.char == 's':  # Move backward
            send_command('B')
        elif key.char == 'd':  # Move right
            send_command('R')
    except AttributeError:
        # Handle special keys (e.g., spacebar for attack)
        if key == keyboard.Key.space:
            send_command('A')  # Attack command (move forward 2x steps)

def on_release(key):
    """Stop sending commands when keys are released."""
    if key == keyboard.Key.esc:  # Stop if Esc key is pressed
        return False

# Start listening to keyboard events
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Control the Arduino with your keyboard (WASD for movement, Spacebar for attack). Press ESC to exit.")

# Keep the script running and control continuous communication
try:
    listener.join()  # Keep the program alive and listening for keyboard inputs
except KeyboardInterrupt:
    print("Program interrupted.")
finally:
    if ser.is_open:
        ser.close()
        print("Serial connection closed")

