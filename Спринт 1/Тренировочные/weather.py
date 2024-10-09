# Хаотичность погоды
# Метеорологическая служба вашего города решила исследовать погоду новым способом.
# Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
# Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго 
# больше, чем в день до (если такой существует) и в день после текущего (если такой существует). 
# Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
# то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
# Определите по ежедневным показаниям температуры хаотичность погоды за этот период.
# Заметим, что если число показаний n=1, то единственный день будет хаотичным.


from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    left_shift = {0}
    right_shift = {len(temperatures) - 1}
    i = 1
    while i <= len(temperatures) - 1:
        j = len(temperatures) - 1 - i 
        if temperatures[i] > temperatures[i-1]:
            left_shift.add(i)
        if temperatures[j] > temperatures[j+1]:
            right_shift.add(j)
        i += 1
    haos = left_shift & right_shift
    return len(haos)


def read_input() -> List[int]:
    _ = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
