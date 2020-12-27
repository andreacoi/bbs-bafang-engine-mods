import os
import communication
import settings


def readresults(name):

    print(f'Hi, {name}')

    logfile = open(settings.logfolder + 'logfile.txt', 'w+')

    logfile.write(communication.results)

    logfile.close()

if __name__ == '__main__':
    readresults('PyCharm')
