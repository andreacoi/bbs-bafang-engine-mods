import serial
import os
import settings

os.chown(settings.path, os.getuid(), os.getgid())
ser = serial.Serial(settings.path, settings.baudrate, settings.timeout, parity=serial.PARITY_EVEN, rtscts = settings.rtscts)

results = ser.readall()