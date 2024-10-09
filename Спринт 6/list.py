# Построить список смежности
# Алла пошла на стажировку в студию графического дизайна, где ей дали такое задание: для 
# очень большого числа ориентированных графов преобразовать их список рёбер в список смежности. 
# Чтобы побыстрее решить эту задачу, она решила автоматизировать процесс.
# Помогите Алле написать программу, которая по списку рёбер графа будет строить его список смежности.


from collections import defaultdict


n, m = map(int, input().split())
edge = []
adj = defaultdict(list)

for i in range(m):
    v1, v2 = list(map(int, input().split()))
    edge.append((v1, v2))
    adj[v1].append(v2)
    
for i in range(1, n+1):
    if adj.get(i, None):
        print(len(adj[i]), ' '.join(map(str, adj[i])))
    else:
        print(0)
        