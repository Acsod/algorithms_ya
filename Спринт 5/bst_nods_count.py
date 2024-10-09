# Разные деревья поиска
# Ребятам стало интересно, сколько может быть различных деревьев поиска, 
# содержащих в своих узлах все уникальные числа от 1 до n. Помогите им 
# найти ответ на этот вопрос.


# (2n)! / (n! * (n+1)!)

def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1) * n


def calculate(nods_count):
    return int(factorial(2 * nods_count) / (factorial(nods_count) * factorial(nods_count + 1)))


print(calculate(int(input())))
