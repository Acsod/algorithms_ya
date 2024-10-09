# Расписание
# Дано количество учебных занятий, проходящих в одной аудитории. Для каждого из них указано 
# время начала и конца. Нужно составить расписание, в соответствии с которым в классе можно 
# будет провести как можно больше занятий.
# Если возможно несколько оптимальных вариантов, то выведите любой. Возможно одновременное 
# проведение более чем одного занятия нулевой длительности.


def read_input() -> dict:
    n = int(input())
    lessons = []
    for i in range(n):
        lessons.append(list(map(float, input().split(' '))))
    return n, lessons


def main():
    n, lessons = read_input()
    lessons.sort(key=lambda x: [x[1], x[0], (x[1] - x[0])])
    answer = [lessons[0],]
    for item in lessons[1:]:
        les = answer[-1]
        if item[0] >= les[1]:
            answer.append(item)
    print(len(answer))
    for i in range(len(answer)):
        print(' '.join(map(str, answer[i])).replace('.0', ''))


main()
