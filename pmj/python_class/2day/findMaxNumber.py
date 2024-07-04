def fn_findMaxNmuber (a,b,c):
    result = a
    if result < b :
        result = b

    if result < c :
        result = c

    return result 

if __name__ == "__main__" :
    a = int(input("값을 입력해주세요"))
    b = int(input("값을 입력해주세요"))
    c = int(input("값을 입력해주세요"))
    print("가장 큰 값은 : " , fn_findMaxNmuber(a,b,c))


