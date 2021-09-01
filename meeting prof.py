def FloydWarshall(graph):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
if __name__ == "__main__":
    while True:
        n = int(input())
        INF = 500 * 26 + 1
        graphY = [[INF if i != j else 0 for i in range(26)] for j in range(26)]
        graphM = [[INF if i != j else 0 for i in range(26)] for j in range(26)]
        if n == 0:
            break
        for _ in range(n):
            lines = list(input().split())
            u = ord(lines[2]) - ord("A")
            v = ord(lines[3]) - ord("A")
            if lines[0] == "Y":
                graphY[u][v] = min(graphY[u][v], int(lines[4]))
                if lines[1] == "B":
                    graphY[v][u] = min(graphY[v][u], int(lines[4]))
            elif lines[0] == "M":
                graphM[u][v] = min(graphM[u][v], int(lines[4]))
                if lines[1] == "B":
                    graphM[v][u] = min(graphM[v][u], int(lines[4]))
        FloydWarshall(graphY)
        FloydWarshall(graphM)
        s, d = input().split()
        s = ord(s) - ord("A")
        d = ord(d) - ord("A")
        minCost = INF
        res = []
        
        for i in range(26):
            cost = graphY[s][i] + graphM[d][i]
            if minCost >= cost:
                minCost = cost
                res.append((cost, i))
                
        if minCost >= INF:
            print("You will never meet.")
        else:
            res.sort()
            print(minCost, end = " ")
            for a, b in res:
                if a > minCost:
                    break
                print(chr(b + ord("A")), end = " ")
            print()