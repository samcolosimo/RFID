import RPi.GPIO as GPIO
import serial
import datetime
import time
from time import ctime
from xlrd import open_workbook
import xlsxwriter

workbook=xlsxwriter.Workbook('test_test_test.xlsx')
worksheet=workbook.add_worksheet()

ser = serial.Serial(port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AL01EX1O-if00-port0',baudrate=2400, timeout=1)

while True:
    response = ser.read(12)
    if response <>"":
        #print "raw: " + str(response)
        print "hex: " + str(response[-8:])
        #print "dec: " + str(int(response[-8:], 16))
        row=0
        col=0
        hexvals=([str(response[-8:])])
        now=datetime.datetime.now()
        input_var = input("Enter Something: ")
        
        #begin excel stuff
        for hexvalue in (hexvals):
            worksheet.write(row, col, hexvalue)
            worksheet.write(row, col+1, "test")
            worksheet.write(row, col+2, format(input_var))
            worksheet.write(row, col+3, ctime())
            row += 1
        workbook.close()

            
            
       
                        
    time.sleep(1)
ser.close()
