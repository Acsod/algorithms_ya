# Золотая лихорадка
# Гуляя по одному из островов Алгосского архипелага, Гоша набрёл на пещеру, в которой лежат
# кучи золотого песка. К счастью, у Гоши есть с собой рюкзак грузоподъёмностью до M килограмм,
# поэтому он может унести с собой какое-то ограниченное количество золота.
# Всего золотых куч n штук, и все они разные. В куче под номером i содержится mi килограммов 
# золотого песка, а стоимость одного килограмма — ci алгосских франков.
# Помогите Гоше наполнить рюкзак так, чтобы общая стоимость золотого песка в пересчёте на алгосские франки была максимальной.


def read_input() -> dict:
    m = int(input())
    n = int(input())
    heaps = []
    for i in range(n):
        heaps.append(list(map(int, input().split(' '))))
    return m, heaps


def main():
    m, heaps = read_input()
    heaps.sort(key=lambda x: [x[0], x[1]], reverse=True)
    weight = 0
    answer = 0
    for heap in heaps:
        can_take = m - weight
        if heap[1] <= can_take:
            weight += heap[1]
            answer += heap[1] * heap[0]
        else:
            weight += can_take
            answer += can_take * heap[0]
    print(answer)


main()
