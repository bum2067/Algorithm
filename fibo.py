n = int(input("수열의 항수를 입력하세요 : "))

# 0번째, 1번째 피보나치 수를 포함하는 배열 생성
answer_arr = [0, 1]

# 반복문을 통해 n을 입력받았을 때, 기존 배열에 n번째 피보나치 수까지 추가
for i in range(n - 1):
    answer_arr.append(answer_arr[1 + i] + answer_arr[i])

# 입력받은 n번째 피보나치 수 출력
print(answer_arr[n])