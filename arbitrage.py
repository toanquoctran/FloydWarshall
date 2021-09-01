def FloydWarshall():
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[i][j] = max(graph[i][j], graph[i][k] * graph[k][j])

if __name__ == "__main__":
    case = 0
    while True:
        n = int(input())      
        graph = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
        if n == 0:
            break
        mapping = {}
        for numOrder in range(n):
            currencies = input()
            mapping[currencies] = numOrder
        m = int(input())
        for _ in range(m):
            souCur, exRate, desCur = input().split()
            graph[mapping[souCur]][mapping[desCur]] = float(exRate)
        input()
        FloydWarshall()
        case += 1
        if graph[mapping[souCur]][mapping[souCur]] > 1:
            print("Case {}: Yes".format(case))
        else:
            print("Case {}: No".format(case))