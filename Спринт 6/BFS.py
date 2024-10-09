# BFS
# Задан неориентированный граф. Обойдите поиском в ширину все вершины, достижимые из
# заданной вершины s, и выведите их в порядке обхода, если начинать обход из s.


from collections import defaultdict, deque


def bfs(adj, root):
    visited = set()
    queue = deque([root])

    visited.add(root)

    while queue:
        v = queue.popleft()
        print(str(v) + " ", end="")

        for neigh in sorted(adj[v]):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)


def main():
    n, m = map(int, input().split())
    edges = []
    adj = defaultdict(list)
    for i in range(m):
        v1, v2 = map(int, input().split())
        edges.append((v1, v2))
        edges.append((v2, v1))
        adj[v1].append(v2)
        adj[v2].append(v1)
    for row in range(1, n + 1):
        if adj.get(row) is None:
            adj[row] = []
    bfs(adj, int(input()))
    

main()
