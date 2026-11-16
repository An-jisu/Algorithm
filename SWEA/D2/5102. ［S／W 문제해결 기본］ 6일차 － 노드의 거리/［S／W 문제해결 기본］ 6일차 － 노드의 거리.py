from collections import deque

def bfs(start, end, V, graph):
    visited = [0] * (V + 1)
    queue = deque([start])
    visited[start] = 1  # 시작점 방문 표시 (거리 0으로 시작하려면 0으로 초기화해도 무방)
    
    while queue:
        curr = queue.popleft()

        # 목적지에 도달한 경우 (방문 배열에 저장된 값 - 시작점 보정 또는 거리 저장 방식)
        if curr == end:
            return visited[curr] - 1

        for next_node in graph[curr]:
            if not visited[next_node]:
                visited[next_node] = visited[curr] + 1
                queue.append(next_node)

    return 0  # 도달할 수 없는 경우


t = int(input())
for test_case in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        u, n = map(int, input().split())
        graph[u].append(n)
        graph[n].append(u)
    start, end = map(int, input().split())
    ans = bfs(start, end, v, graph)
    print(f"#{test_case} {ans}")