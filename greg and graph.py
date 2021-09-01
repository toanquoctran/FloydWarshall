def FloydWarshall():
    res = [0] * n
    for vertice in range(n - 1, -1, -1):
        k = deletedVertices[vertice]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
        for i in deletedVertices[vertice:]:
            for j in deletedVertices[vertice:]:
                res[vertice] += graph[i][j]
    
    return res
    
if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    graph = [[INF if i != j else 0 for i in range(n + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1):
        lines = list(map(int, input().split()))
        for j in range(1, n + 1):
            graph[i][j] = lines[j - 1]
            
    deletedVertices = list(map(int, input().split()))   
    
    print(*FloydWarshall())