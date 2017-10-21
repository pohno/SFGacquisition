# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:01:41 2017

@author: Geiger
"""
import serial

class TOPAS():

    def __init__(self):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = 'COM1'
        
        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 19200
        
        #timeout after 1 second so don't wait forever
        ser.timeout = 1
        
        self.ser = ser
        
    def getStatus(self):
        self.ser.write('GetStatus')
        return self.ser.read()
        
        
    def getWavelength(self):
        self.ser.write('GetWavelength')
        return self.ser.read()
    
    def setWavelength(self,wavelength):
        #numbers should set interaction as DFG1
        self.ser.write('SetWavelengthEx ' + str(wavelength) + '1,6,0,0' )
    
    def closeShutter(self):
        self.ser.write('CloseShutter')
        
    def openShutter(self):
        self.ser.write('OpenShutter')