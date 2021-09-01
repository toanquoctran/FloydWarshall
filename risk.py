def FloydWarshall():
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
if __name__ == "__main__":
    INF = int(1e9)
    case = 1
    while True:
        try:
            graph = [[INF if i != j else 0 for i in range(21)] for j in range(21)]
            for i in range(19):
                lines = list(map(int, input().split()))
                for j in range(lines[0]):
                    graph[i + 1][lines[j + 1]] = 1
                    graph[lines[j + 1]][i + 1] = 1
                    
            FloydWarshall()
            
            print("Test Set #{}".format(case))
        
            n = int(input())
            for _ in range(n):
                s, e = map(int, input().split())
                print("{:2d} to {:2d}: {}".format(s, e, graph[s][e]))
            
            print()
            case += 1
        except EOFError:
            break