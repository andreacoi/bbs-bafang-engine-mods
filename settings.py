from pathlib import Path

baudrate = 1200
path = '/dev/ttyUSB0'
parity = 'PARITY_EVEN'
logfolder = '/archivio/triride/'
home = str(Path.home())
logfolder = home + logfolder
timeout = 0
rtscts = 1
