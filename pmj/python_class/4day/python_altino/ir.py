from AltinoLite import *

Open()

#적외선 센서 초기화
#IRSet()

#while 1 :
#   print("프론트 왼쪽" + str(sensor.IR[1]) + " 프론트 센터" + str(sensor.IR[2]) + " 프론트 오른쪽" + str(sensor.IR[3]))

Go(300,300)
flag = 1
while 1 :
    print("프론트 왼쪽" + str(sensor.IR[1]) + " 프론트 센터" + str(sensor.IR[2]) + " 프론트 오른쪽" + str(sensor.IR[3]) + " 프론트 뒤쪽" + str(sensor.IR[6]))
    
    if sensor.IR[2] > 20:
        if flag == 1 :
            Go(0,0)
            flag = 0
        for i in range(0,1) :
            Light(12)   
            delay(500)
            Light(0)
            delay(500)
        Go(-300,-300)   
        
    elif sensor.IR[6] > 20 :
        if flag == 0 :
            Go(0,0)
            flag = 1
        for i in range(0,1) :
            Light(12)   
            delay(500)
            Light(0)
            delay(500)
        Go(300,300)

Close()

