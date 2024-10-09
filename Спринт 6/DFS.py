# DFS
# Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые из
# заданной вершины s, и выведите их в порядке обхода, если начинать обход из s.


from collections import defaultdict


def dfs(adj, start_v):
    stack = []
    visited = set()
    stack.append(start_v)
    result = []
    while stack:
        v = stack.pop()
        if v not in visited:
            result.append(v)
            visited.add(v)
            vs = adj[v]
            for new_v in reversed(sorted(vs)):
                stack.append(new_v)
    return result


def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        v1, v2 = map(int, input().split())
        edges.append((v1, v2))
    adj = defaultdict(list)
    for i in edges:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    start_v = int(input())
    print(*dfs(adj, start_v))


main()
