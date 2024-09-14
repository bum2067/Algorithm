import random
import time
import matplotlib.pyplot as plt


# 버블 정렬 함수
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 퀵 정렬 함수
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 합병 정렬 함수
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# 합병하는 부분
def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return sorted_arr


# 메인 함수
def main():
    # 데이터 갯수 입력
    num_elements = int(input("Enter the number of elements: "))

    # 입력받은 갯수만큼 랜덤 리스트 생성
    data = [random.randint(1, 1001) for _ in range(num_elements)]

    # 원본 데이터 출력
    print("Original data:", data)

    # 버블 정렬 실행 및 시간 측정
    start_time = time.time()
    bubble_sorted = bubble_sort(data.copy())
    bubble_time = time.time() - start_time
    print(f"Bubble sort result: {bubble_sorted} (Time: {bubble_time:.6f} seconds)")

    # 퀵 정렬 실행 및 시간 측정
    start_time = time.time()
    quick_sorted = quick_sort(data.copy())
    quick_time = time.time() - start_time
    print(f"Quick sort result: {quick_sorted} (Time: {quick_time:.6f} seconds)")

    # 합병 정렬 실행 및 시간 측정
    start_time = time.time()
    merge_sorted = merge_sort(data.copy())
    merge_time = time.time() - start_time
    print(f"Merge sort result: {merge_sorted} (Time: {merge_time:.6f} seconds)")

    # 그래프 그리기
    fig, axs = plt.subplots(3, figsize=(8, 12))  # 3개의 서브 플롯 생성

    # 버블 정렬 결과 그래프 (막대 그래프)
    axs[0].bar(range(len(bubble_sorted)), bubble_sorted, color='blue')
    axs[0].set_title(f'Bubble Sort (Time: {bubble_time:.6f} sec)')

    # 퀵 정렬 결과 그래프 (막대 그래프)
    axs[1].bar(range(len(quick_sorted)), quick_sorted, color='green')
    axs[1].set_title(f'Quick Sort (Time: {quick_time:.6f} sec)')

    # 합병 정렬 결과 그래프 (막대 그래프)
    axs[2].bar(range(len(merge_sorted)), merge_sorted, color='red')
    axs[2].set_title(f'Merge Sort (Time: {merge_time:.6f} sec)')

    # 그래프 간격 조정
    plt.tight_layout()

    # 그래프 보여주기
    plt.show()


if __name__ == "__main__":
    main()
