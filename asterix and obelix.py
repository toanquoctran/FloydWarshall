def FloydWarshall():
    for i in range(1, c + 1):
        for j in range(1, c + 1):
            maxCost[i][j] = max(costs[i - 1], costs[j - 1])
    for i in range(c + 1):
        for j in range(c + 1):
            for k in range(c + 1):
                temp = max(maxCost[i][k], maxCost[k][j])
                if graph[i][j] + maxCost[i][j] > graph[i][k] + graph[k][j] + temp:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    maxCost[i][j] = temp
    
if __name__ == "__main__":
    INF = int(1e9)
    case = 1
    while True:
        c, r, q = map(int, input().split())
        if c == 0 and r == 0 and q == 0:
            break
        
        graph = [[INF if i != j else 0 for i in range(c + 1)] for j in range(c + 1)]
        maxCost = [[0 for _ in range(c + 1)] for _ in range(c + 1)]
        costs = list(map(int, input().split()))
        
        for _ in range(r):
            c1, c2, d = map(int, input().split())
            graph[c1][c2] = d
            graph[c2][c1] = d
            
        FloydWarshall()
        print("Case #{}".format(case))
        case += 1
        
        for _ in range(q):
            s, d = map(int, input().split())
            if graph[s][d] + maxCost[s][d] >= INF:
                print(-1)
            else:
                print(graph[s][d] + maxCost[s][d])
        print()