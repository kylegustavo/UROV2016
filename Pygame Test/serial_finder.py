import glob
import sys
import serial
from sys import platform

import pygame
from pygame.locals import *


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


def find_port(ports,background, screen):

    writeonscreen = "Possible ports: "
    font = pygame.font.Font(None, 25)
    text = font.render(writeonscreen, 0, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 75
    textpos.centery = 10
    background.blit(text, textpos)

    screen.blit(background, (0, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return

    if platform == "linux" or platform == "linux2":
        count  = 0
        for p in ports:
            writeonscreen = str(p)
            font = pygame.font.Font(None, 50)
            text = font.render(writeonscreen, 0, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = 175 + 65* count
            textpos.centery = 10
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            count += 1

            if "USB" in p:

                writeonscreen = "Connected To: " + str(p)
                font = pygame.font.Font(None, 50)
                text = font.render(writeonscreen, 0, (10, 10, 10))
                textpos = text.get_rect()
                textpos.centerx = background.get_rect().centerx - 50
                textpos.centery = background.get_rect().centery
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
                pygame.display.flip()

                return p
    elif platform == "darwin":
        p = ""
    elif platform == "win32":
        p = ""
        count = 0
        for p in ports:

            writeonscreen = str(p)
            font = pygame.font.Font(None, 25)
            text = font.render(writeonscreen, 0, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = 175 + 65*count
            textpos.centery = 10
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            count += 1

        return p

            
