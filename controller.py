from re import I
import pyautogui
import time
import serial

arduino = serial.Serial('com6', 9600)

def analyze_signal():
    
    signal = str(arduino.readline())
    
    print(signal)

    if 'stop' in signal:
        pyautogui.typewrite(['space'], 0.2)
        time.sleep(0.2)
    
    elif 'back' in signal:
        pyautogui.hotkey('ctrl', 'left')
        time.sleep(0.2)

    elif 'next' in signal:
        pyautogui.hotkey('ctrl', 'right')
        time.sleep(0.2)

while True:

    analyze_signal()





