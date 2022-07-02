import time
import threading
import tkinter
import pyttsx3
from tkinter import ttk
from tkinter import *
import serial
import pyautogui
import os
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()


def fun(serial_data, text):
    if 'B44B9B44' in serial_data:
        text.insert(END, 'volume up\n')
        pyautogui.press('volumeup', 10)
    elif '20DFC03F' in serial_data:
        pyautogui.press('volumedown', 10)
    elif '20DF00FF' in serial_data:
        pyautogui.press('pageup')
    elif '20DF807F' in serial_data:
        pyautogui.press('pagedown')
    elif 'F9069B44' in serial_data:
        text.insert(END, 'start button\n')
        pyautogui.press('win')
