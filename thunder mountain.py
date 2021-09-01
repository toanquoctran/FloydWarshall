import math

def FloydWarshall():
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if __name__ == "__main__":
    tc = int(input())
    INF = int(1e9)
    for case in range(tc):
        n = int(input())
        x = [None] * n
        y = [None] * n
        case += 1
        graph = [[0 if i == j else INF for i in range(n)] for j in range(n)]

        for i in range(n):
            x[i], y[i] = map(int, input().split())

        for i in range(n):
            for j in range(n):
                dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
                if dist <= 10:
                    graph[i][j] = dist
                    graph[j][i] = dist

        FloydWarshall()
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(graph[i][j], res)
                
        print("Case #{}:".format(case))
        if res != INF:
            print(format(res, ".4f"))
        else:
            print("Send Kurdy")
        print()