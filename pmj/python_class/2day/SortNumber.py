def fn_SortNumber(arr) :

    for i in range(0,10) :
        for x in range(0, 10) :
            if ( arr[i] < arr[x] ) :
                tmp = arr [x]
                arr[x] = arr[i]
                arr[i] = tmp

    return arr

arr = []
for i in range(0,10) :
    arr.append(int(input( str(i) + "번째 숫자를 입력하세요 !")))
    
a = fn_SortNumber(arr)

for i in a :
    print(i)