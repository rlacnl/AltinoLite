#사용자로부터 2진수를 입력받음

from unittest import result


userNumber = input("1바이트 2진수를 입력하세요. ( 최대 8자리 ) : ")

#사용자 입력 값검증
if len(userNumber) > 8 :
    print("1바이트를 초과하는 2진수입니다")
    exit()

#10진수 변환
cnt = 128 
result = 0

for i in userNumber.rjust(8,'0'):
    result += int(i) * cnt
    cnt = cnt // 2

print(result)
    
    

