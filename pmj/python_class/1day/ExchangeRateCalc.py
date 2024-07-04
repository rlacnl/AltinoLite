exchageRate = float(input("현재 기준 원화 환율을 (1달러) 입력하세요: "))
amount = float(input("환전 희망 금액(원)을 입력하세요: "))

result = amount / exchageRate

print("환전 금액은 " + str(round(result, 2)) + "달러 입니다")