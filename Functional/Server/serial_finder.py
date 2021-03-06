import glob
import sys
import serial
from sys import platform


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        s = 0
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def find_port(ports):
    print "Possible ports: ",
    if platform == "linux" or platform == "linux2":
        for p in ports:
            print p, " ",
            if "USB" in p:
                print "Connected To: ", p
                return p
    elif platform == "darwin":
        p = ""
    elif platform == "win32":
        p = ""
        for p in ports:
            print p
        return p

            
