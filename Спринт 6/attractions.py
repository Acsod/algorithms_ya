# Достопримечательности
# Вы приехали на архипелаг Алгосы (наконец-то!). Здесь есть n достопримечательностей. 
# Ваша лодка может высадить вас у одной из них, забрать у какой-то другой, возможно, 
# той же самой достопримечательности и увезти на материк.
# Чтобы более тщательно спланировать свой маршрут, вы хотите узнать расстояния между 
# каждой парой достопримечательностей Алгосов. Некоторые из них соединены мостами, по 
# которым вы можете передвигаться в любую сторону. Всего мостов m.
# Есть вероятность, что карта архипелага устроена так, что нельзя добраться от какой-то
# одной достопримечательности до другой без использования лодки.
# Найдите кратчайшие расстояния между всеми парами достопримечательностей.


n, m = map(int, input().split())
graph = [[float("inf")] * n for _ in range(n)]

for i in range(m):
    u, v, l = map(int, input().split())
    if graph[u - 1][v - 1] == float("inf"):
        graph[u - 1][v - 1] = l
        graph[v - 1][u - 1] = l

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:
    for item in row:
        print(item if item != float("inf") else -1, end=' ')
    print()
    