from AltinoLite import *
import pygame

def altinoSound(soundFileName):
    pygame.mixer.init()
    pygame.mixer.music.load("D:\\pmj\\AltinoLite-1\\pmj\\python_class\\4day\\python_altino\\" + soundFileName)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

altinoSound("start.mp3")

Open()

altinoSound("_con.mp3")

while 1 :
    Go(300,300)
    altinoSound("Go.mp3")
    Delay(3000)
    Go(0,0)
    altinoSound("Que.mp3")
    command = int(input("1 : 다시 출발 / 2 : 이제 그만"))
    if command == 1 :
        continue
    else :
        break


Close()