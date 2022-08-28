# Copyright Ⓒ Fabio Brunner (fabsg0) [2022]
# https://github.com/fabsg0/ArduinoControlledSpotify/


# Import pyautogui, time and the serial communication
import pyautogui
import time
import serial


# Initializes the communication between the Arduino and the python script
arduino = serial.Serial('com6', 9600)

def analyze_signal():
    
    signal = str(arduino.readline())
    
    print(signal)

    # If the Arduino sends the 'stop' signal, the script presses the virtual space button.
    if 'stop' in signal: 
        pyautogui.typewrite(['space'], 0.2)
        time.sleep(0.2)
    
    # If the Arduino sends the 'back' signal, the script presses the hotkey Control + left.
    elif 'back' in signal:
        pyautogui.hotkey('ctrl', 'left')
        time.sleep(0.2)

    # If the Arduino sends the 'next' signal, the script presses the hotkey Control + right.
    elif 'next' in signal:
        pyautogui.hotkey('ctrl', 'right')
        time.sleep(0.2)


# you need the while loop, that the script doesn't closes automatically.
while True:

    analyze_signal()





