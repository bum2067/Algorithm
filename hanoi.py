# 하노이 탑 재귀 함수
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"원판 1을 {source}에서 {target}으로 이동")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"원판 {n}을 {source}에서 {target}으로 이동")
    hanoi(n - 1, auxiliary, target, source)

# 사용자로부터 원판의 개수를 입력받음
n = int(input("원판의 개수를 입력하세요: "))
print(f"총 {n}개의 원판을 {n}번의 이동으로 해결할 수 있습니다.\n")

# 하노이 탑 함수 호출 (출발지: A, 목표지: C, 보조지: B)
hanoi(n, 'A', 'C', 'B')
