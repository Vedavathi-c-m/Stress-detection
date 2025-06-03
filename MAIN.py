import serial
import time
import os

data = serial.Serial(
                    'COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )

def Send(a):
  data.write(str.encode(a))
  print('sent............')

def Read():
  print("reading")
  while True:
    Data = data.readline()
    Data = Data.decode('utf-8', 'ignore')
    # print("Raw data is ---- {}  ---".format(Data))
    Data = Data.split(',')
    print(Data)
    Data=Data[0]
##    for item in Data:
    if 'X' in Data.strip():
      print("Found 'X'")
      break
    else:
      print("'X' not found")
  return Data

dat=Read()
if 'X' in dat.strip():
  from test import run
  run()
