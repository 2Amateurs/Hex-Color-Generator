import datetime
import pygame, sys
from pygame.locals import *
import math
import time
import nameMaker


daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

now = datetime.datetime.now()
start = datetime.datetime(now.year, 1, 1)
day = (now - start).days + 1
print("Today is " + daysOfWeek[now.weekday()] + ", " + months[now.month-1] + " " + str(now.day))

pygame.init()
def hex(rgb):
    return '#%02x%02x%02x' % rgb
def getColor():
    function = int((0.0437499162265*day)**2)
    gunction = int(math.sin(day)*127.5*(math.e**(-0.01*day))+127.5)
    green = int(abs(15+function-gunction))
    red = int(1.39726027397 * math.sqrt(182.5**2-(day-182.5)**2))
    blue = int(255-red)
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
