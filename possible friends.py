def FloydWarshall():
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "Y":
                dist[i][j] = 1
            else:
                if i == j:
                    dist[i][j] = 0
                else:
                    dist[i][j] = INF
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
               
    return dist
            
if __name__ == "__main__":
    INF = 1000
    t = int(input())
    for _ in range(t):
        matrix = []
        firstLine = input()
        n = len(firstLine)
        matrix.append(firstLine)
        for i in range(n - 1):
            matrix.append(input())
            
        dist = FloydWarshall()
        res = 0
        index = 0
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] == 2:
                    count += 1
            if count > res:
                res = count
                index = i
        print(index, res)