'''
Name: Jens Daci 
Date: 02/24/2019

Code Description:
	Python file to graph arduino serial data in real time. 
	Used for the handwriting UREP Project.
	Shows the range for appropriate force.
	Saves the data gathered from the serial in a text file.
'''

import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *

sensor1_array = []
sensor2_array = []
sensor3_array = []


def makeFig():

	plt.ylim(0, 10)
	plt.title("Live Sensor Data")
	plt.grid(True)
	plt.ylabel("Force [N]")
	plt.plot(sensor1_array, "ro-", label = "Thumb Force [N]")
	plt.legend(loc = "upper left")
	
	plt2 = plt.twinx()
	plt.ylim(0, 10)
	plt2.plot(sensor2_array, "b^-", label = "Index Finger Force [N]")
	plt2.set_ylabel("")
	plt2.legend(loc = "upper right")
	
	plt3 = plt.twinx()
	plt.ylim(0, 10)
	plt3.plot(sensor3_array, "c^-", label = "Middle Finger Force [N]")
	plt3.legend(loc = "lower left")
	
	plt.axhline(y = 15, color = "y", linestyle = "--")
	plt.axhline(y = 10, color = "y", linestyle = "--")
	
def startGraph():
        com_port_number = input("Enter the com_port number: ")
        arduinoData = serial.Serial("com" + str(com_port_number), 19200)
        plt.ion()
        cnt = 0
        filename = input("Enter the name of the file: ")
        print("Start Writing with The Grip...")
                
        while True: 
                while (arduinoData.inWaiting() == 0):
                        pass
                
                arduinoString = arduinoData.readline()
                arduinoStr = arduinoString.decode().split(",")
                
                sensor1 = float(arduinoStr[0])
                sensor2 = float(arduinoStr[1])
                sensor3 = float(arduinoStr[2])
                
                sensor1_array.append(sensor1)
                sensor2_array.append(sensor2)
                sensor3_array.append(sensor3)
                
                
                with open(filename + ".txt", "w") as f:
                        for i in range(0, len(sensor1_array)):
                                f.write(str(sensor1_array[i]) + ", " + str(sensor2_array[i]) + ", " + str(sensor3_array[i]) + "\n")
                
                drawnow(makeFig)
                plt.pause(0.000001)
                cnt = cnt + 1
                
                ''' Better representation for the graph
                if (cnt > 30):
                        sensor1_array.pop(0)
                        sensor2_array.pop(0)
                '''
	
	
	
	

