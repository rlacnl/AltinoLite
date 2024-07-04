import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import speech_recognition as sr
from AltinoLite import *
import pygame

f1Sum = 0
f2Sum = 0
f3Sum = 0
r4Sum = 0
l5Sum = 0
b6Sum = 0

f1Avr = 0
f2Avr = 0
f3Avr = 0
r4Avr = 0
l5Avr = 0
b6Avr = 0

cnt = 1   # 평균 카운트

def inputAudio():
    # 음성 인식기 인스턴스 생성
    recognizer = sr.Recognizer()

    # 마이크를 음성 소스로 사용
    with sr.Microphone() as source:
        print("말씀해 주세요...")
        
        # 잡음 수준을 자동으로 조정
        recognizer.adjust_for_ambient_noise(source)
        
        # 음성을 들음
        audio_data = recognizer.listen(source)
        
        try:
            # 음성을 텍스트로 변환 (한글 인식)
            text = recognizer.recognize_google(audio_data, language='ko-KR')
            print(f"인식된 텍스트: {text}")
            return str(text)  # Return the recognized text
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
            return None  # Return None if recognition fails
        except sr.RequestError as e:
            print(f"구글 음성 인식 서비스에 문제가 있습니다: {e}")
            return None  # Return None if there's an error with Google service

def Gear() :
    global f1Sum
    global f2Sum
    global f3Sum
    global r4Sum
    global l5Sum
    global b6Sum

    global f1Avr
    global f2Avr
    global f3Avr
    global r4Avr
    global l5Avr
    global b6Avr
    global cnt

    f1Sum += sensor.IR[1]
    f2Sum += sensor.IR[2]
    f3Sum += sensor.IR[3]
    r4Sum += sensor.IR[4]
    l5Sum += sensor.IR[5]
    b6Sum += sensor.IR[6]

    f1Avr = f1Sum // cnt
    f2Avr = f2Sum // cnt
    f3Avr = f3Sum // cnt
    r4Avr = r4Sum // cnt
    l5Avr = l5Sum // cnt
    b6Avr = b6Sum // cnt

    cnt += 1

    if cnt > 3 :
        cnt = 1
        f1Sum = 0
        f2Sum = 0
        f3Sum = 0
        r4Sum = 0
        l5Sum = 0
        b6Sum = 0

def Trun() :
    Gear()
    Go(300,300)

    print(str(r4Avr) +":"+str(f3Avr) + ":" + str(l5Avr) +":"+str(f1Avr))

    if (r4Avr > 20 or f3Avr > 20) :
        #print("오른쪽")
        i = -10 + -r4Avr + -f3Avr
        if i > 127 :
            i = 127
        Steering(i)
    elif (l5Avr > 20 or f1Avr > 20) :
        #print("왼쪽")
        i = 10 + l5Avr + f1Avr
        if i > 127 :
            i = 127
        Steering(i)
    elif (r4Avr <= 30) :
        #print("오른쪽")
        Steering(0)
    elif (l5Avr <= 30) :
        #print("왼쪽")
        Steering(0)

def Left() :
    Go(300,300)
    Steering(-127)
    Delay(4000)
    Steering(0)
    Go(300,300)

def Right() :
    Go(300,300)
    Steering(3200)
    Delay(4000)
    Steering(0)
    Go(300,300)

# def Trun() :
#     Gear()
#     Go(300,300)

#     print(str(r4Avr) +":"+str(f3Avr) + ":" + str(l5Avr) +":"+str(f1Avr))

#     if (r4Avr >= 30 or f3Avr >= 30) :
#         #print("오른쪽")
#         i = -30 + -r4Avr + -f3Avr
#         if i > 127 :
#             i = 127
#         Steering(i)   
#     elif (l5Avr >= 30 or f1Avr >= 30) :
#         #print("왼쪽")
#         i = 30 + l5Avr + f1Avr
#         if i > 127 :
#             i = 127
#         Steering(i)
#     elif (r4Avr <= 50) :
#         #print("오른쪽")
#         Steering(0)
#     elif (l5Avr <= 50) :
#         #print("왼쪽")
#         Steering(0)

def altinoSound(soundFileName):
    pygame.mixer.init()
    pygame.mixer.music.load("D:\\pmj\\AltinoLite-1\\pmj\\python_class\\4day\\python_altino\\" + soundFileName)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

altinoSound("start.mp3")


# form_class = uic.loadUiType("altino.ui")[0]

# class MyWindow(QMainWindow, form_class):
#     def __init__(self) :
#         super().__init__()
#         self.setupUi(self)

#         # 내가 원하는 기능들을 추가
        

# if __name__ == "__main__" :
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

Open()

first = True

# Main control loop
while True:
    Trun()

    if sensor.CDS >= 1500:
        Go(0, 0)
        altinoSound("Que.mp3")

        result = ""
        while first:
            result = inputAudio()
            if result == "앞으로가" or result == "오른쪽으로가" :
                break
            else:
                altinoSound("result.mp3")

        if result == "앞으로가":
            first = False
            Trun()
            Delay(1500)
        elif result == "오른쪽으로가":
            first = False
            Right()
            Trun()

            if sensor.CDS >= 1500 :
                altinoSound("Que.mp3")

        result = ""
        while first:
            result = inputAudio()
            if result == "앞으로가" or result == "왼쪽으로가" :
                break
            else:
                altinoSound("result.mp3")

        if result == "앞으로가":
            first = False
            Trun()
            Delay(1500)
        elif result == "왼쪽으로가":
            first = False
            Left()
            Trun()


            

# Clean up and close Altino when loop breaks
Close()