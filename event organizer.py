def FloydWarshall():
    for i in range(49):
        for j in range(49):
            for k in range(49):
                if i <= k <= j:
                    graph[i][j] = max(graph[i][j], graph[i][k] + graph[k][j])

if __name__ == "__main__":
    t = int(input())
    INF = int(1e9)
    for _ in range(t):
        n = int(input())
        graph = [[0 for i in range(49)] for j in range(49)]

        for _ in range(n):
            s, e, c = map(int, input().split())
            graph[s][e] = max(c, graph[s][e])
        
        FloydWarshall()
        print(graph[0][48])