# Банкомат
# Тимофей пошёл снять деньги в банкомат. Ему нужно m франков. В банкомате в 
# бесконечном количестве имеются купюры различных достоинств. Всего различных
# достоинств n. Купюр каждого достоинства можно взять бесконечно много. Нужно 
# определить число способов, которыми Тимофей сможет набрать нужную сумму.


def get_money(need, coins):
    combins = [0] * (need + 1)
    combins[0] = 1
    for coin in coins:
        for j in range(len(combins)):
            if j >= coin:
                combins[j] += combins[j - coin]
    return combins[need]


def main():
    need = int(input())
    n = int(input())
    coins = list(map(int, input().split()))
    print(get_money(need, coins))


main()
