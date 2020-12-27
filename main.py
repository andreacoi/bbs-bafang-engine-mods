import os
import communication
import settings
from pathlib import Path

def readresults(name):

    print(f'Hi, {name}')
    home = str(Path.home())
    logfile = open(home + settings.logfolder + 'logfile.txt', 'w+')

    logfile.write(communication.results)

    logfile.close()

if __name__ == '__main__':
    readresults('PyCharm')
