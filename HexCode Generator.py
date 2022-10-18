import datetime
import pygame, sys
from pygame.locals import *
import math
import time
import nameMaker


daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

now = datetime.datetime.today()
day = now.timetuple().tm_yday

print("Today is " + daysOfWeek[now.weekday()] + ", " + months[now.month-1] + " " + str(now.day))

pygame.init()
def hex(rgb):
    return '#%02x%02x%02x' % rgb
def getColor():
    green = int(abs(math.sqrt(24025 - (0.424*day)**2)+100*math.cos(255*3.14*day)))
    red = int(127.5*math.cos(day)+127.5)
    blue = int(0.0019*(day**2))
    color = red, green, blue
    print(hex(color))
    screen = pygame.display.set_mode((900, 600))
    screen.fill(color)
    pygame.display.update()

getColor()
nameMaker.getName()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
