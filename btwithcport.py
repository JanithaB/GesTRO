import serial
import pyautogui
import mouse
import cportn
from threading import Thread

#detect COM port
global comport
comport = cportn.detect_esp32_com_port()
#print (comport)


ser =serial.Serial(comport,9600,timeout = 1)
pyautogui.FAILSAFE=False
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0

#function to check connection between bluetooth module
def connection():
     
     if comport:
          #print("1")
          return 1
     else:
          #print("0")
          return None


def retrieveData():
    
    ser.write(b'1')
    
    data = ser.readline().decode('ascii')
    return data
    
slider_val = 6

def save(value):
        global slider_val
        slider_val = int(value)
        print(slider_val)


def infinite_loop(ser,slider_val):
    #print (slider_val)
    if comport:
        sp_data = retrieveData()
        d5=0
        d6=0
        while(True):


    
            sp_data=retrieveData().split()
            d1=int(sp_data[0])
            d2=int(sp_data[1])
            pyautogui.PAUSE = 0
            pyautogui.move(d1,d2,duration=0)
            d3=int(sp_data[2])
            d4=int(sp_data[3])

            if(d3>0):
                 d5=1
                 pyautogui.mouseDown()
                 #mouse.click('left')
            elif(d3==0):
                 if(d5>0):
                      pyautogui.mouseUp()
                      d5=0
                 
                 elif(d4>0):
                 #mouse.click('right')
                      d6=1
                 
                 elif(d4==0):
                      if(d6>0):
                           mouse.click('right')
                           d6=0
                 
                 
            
            #print(sp_data)
    elif(OSError, serial.SerialException):
         connection = None
         pass


thread = Thread(target=infinite_loop,args=(ser,slider_val,))
thread.daemon = True
thread.start()
    
    
