import time, threading, tkinter ,pyttsx3
from tkinter import ttk
from tkinter import *
import serial, pyautogui ,os
import serial.tools.list_ports
ports=serial.tools.list_ports.comports()
from keybindings import fun

# print ("list of COM ports: \n")
# for port, desc,hwid in sorted(ports):
#     print("{}: {} ".format(port, desc))


serial_data = ''
filter_data = ''
update_period = 1
serial_object = None
cn = False

gui = Tk()
gui.title("REMOTE CONTROL")
gui.configure(background="whitesmoke")


def connect():
    global serial_object
    port = port_entry.get()
    baud = 115200
    try:
        serial_object = serial.Serial('COM'+ str(port), baud)
    except:
        print ("Enter Baud and Port")
        text.insert(END, "Please enter the port no.")
        return
    Label(text="Connected to IR Receiver",font="Times 15 " ,fg="green", bg="whitesmoke").place(x=80, y=130)
    # pyttsx3.speak("Connected to IR Receiver")
    t1 = threading.Thread(target = get_data)
    t1.daemon = True
    t1.start()


def get_data():
    global serial_object
    global filter_data

    while(1):   
        try:
            serial_data = serial_object.readline()
            refined=str(serial_data.decode('ascii'))
            
            serial_data=refined
           
            text.insert(END, serial_data)
            fun(serial_data , text)
            
        except TypeError:
            pass

def update_gui():
    global filter_data
    global update_period
    global serial_object
    
    text.place(x = 12, y = 170)
    new = time.time()
        
    while(1):
        if time.time() - new >= update_period:
            text.delete(0.0, END)
            new = time.time()

def disconnect():
    try:
        serial_object.close() 
    except AttributeError:
        print ("Exited..")
    gui.destroy()
    gui.quit()


##############################################


if __name__ == "__main__":
    text = Text(width = 59, height = 7 ,font="Consolas 11 bold  ", fg="green" , bg="black")
    text.insert(END , "\t\t     <<< WELCOME >>>")
    
    t2 = threading.Thread(target = update_gui)
    t2.daemon = True
    t2.start()

    Label(text="Mini Project",font="Times 25 bold italic ", bg="whitesmoke" , fg="blue").place(x=150, y=30)
    Label(text="IR REMOTE PC CONTROL",font="Times 15 bold ", bg="whitesmoke").place(x=120, y=80)

    Label(text = "Port:",font="Times 15 ",width=6 , bg="whitesmoke").place(x = 360, y = 130)
    Label(text="Status:",font="Times 15 ", bg="whitesmoke").place(x=12, y=130)

    Label(text="Disconnected",font="Times 15 ",fg="red" , bg="whitesmoke").place(x=80, y=130)

    port_entry = Entry(width = 5,font="Times 14" )
    port_entry.place(x = 435, y = 131)

    Button(text = "Connect", command = connect).place(x = 10, y = 320)
    Button(text = "Exit", command = disconnect,width=10).place(x =408, y = 320)

    gui.geometry('500x370')
    gui.resizable(0,0)
    gui.mainloop()

   