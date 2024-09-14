import math
import random
import matplotlib.pyplot as plt


# 두 점 사이의 거리 계산
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 최근접점쌍 찾기 (분할정복)
def closest_pair(points):
    # 점이 3개 이하인 경우는 직접 계산
    if len(points) <= 3:
        min_dist = float('inf')
        p1, p2 = None, None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    p1, p2 = points[i], points[j]
        return p1, p2, min_dist

    # 중간을 기준으로 분할
    mid = len(points) // 2
    mid_point = points[mid]

    # 좌우로 나누어 각각 최근접점을 찾음
    left_points = points[:mid]
    right_points = points[mid:]

    (p1_left, p2_left, dist_left) = closest_pair(left_points)
    (p1_right, p2_right, dist_right) = closest_pair(right_points)

    # 왼쪽과 오른쪽 중 더 작은 거리 선택
    if dist_left < dist_right:
        d_min = dist_left
        p1, p2 = p1_left, p2_left
    else:
        d_min = dist_right
        p1, p2 = p1_right, p2_right

    # 중간 영역에서의 최근접점 찾기
    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < d_min:
            strip.append(point)

    # strip 내부에서 거리 비교
    strip.sort(key=lambda point: point[1])  # y좌표 기준 정렬
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = distance(strip[i], strip[j])
            if d < d_min:
                d_min = d
                p1, p2 = strip[i], strip[j]

    return p1, p2, d_min


# 그래픽으로 점과 최근접점쌍을 보여주는 함수
def plot_points(points, closest_points):
    # 점들 플로팅
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]

    plt.scatter(x_vals, y_vals, label="Points", color="blue")

    # 최근접점쌍 강조
    p1, p2 = closest_points
    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color="red", label="Closest Pair")

    # 선 그리기
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r--')

    # 그래프 설정
    plt.title("Closest Pair of Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()


# 랜덤 좌표 생성 함수 (소수점 둘째자리까지)
def generate_random_points(num_points, range_min=-100, range_max=100):
    points = []
    for _ in range(num_points):
        x = round(random.uniform(range_min, range_max), 2)
        y = round(random.uniform(range_min, range_max), 2)
        points.append((x, y))
    return points


# 메인 함수
def main():
    # 사용자로부터 좌표의 갯수 입력
    num_points = int(input("생성할 점의 갯수를 입력하세요: "))

    # 랜덤 점 생성
    points = generate_random_points(num_points)

    # x좌표 기준으로 정렬
    points.sort()

    # 최근접점쌍 찾기
    p1, p2, min_dist = closest_pair(points)
    print(f"가장 가까운 두 점: {p1}와 {p2}")
    print(f"최소 거리: {min_dist:.4f}")

    # 그래픽으로 표시
    plot_points(points, (p1, p2))


if __name__ == "__main__":
    main()
