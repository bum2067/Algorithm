import random

# 무한대 값 정의 (경로가 없는 경우)
INF = float('inf')


def generate_random_graph(num_vertices, max_weight=10, density=0.5):
    """
    무작위 가중치로 그래프 생성
    - num_vertices: 정점 수
    - max_weight: 가중치의 최대값
    - density: 밀도 (0~1 사이의 값으로, 1에 가까울수록 간선이 많음)
    """
    graph = [[INF if i != j else 0 for j in range(num_vertices)] for i in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and random.random() < density:
                graph[i][j] = random.randint(1, max_weight)

    return graph


def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# 사용자 입력
num_vertices = int(input("정점의 수를 입력하세요: "))
graph = generate_random_graph(num_vertices)

# 무작위로 생성된 그래프 출력
print("무작위로 생성된 그래프:")
for row in graph:
    print(row)

# 플로이드-워셜 알고리즘 실행
shortest_paths = floyd_warshall(graph)

# 최단 경로 출력
print("\n모든 쌍 최단 경로 행렬:")
for row in shortest_paths:
    print(row)
