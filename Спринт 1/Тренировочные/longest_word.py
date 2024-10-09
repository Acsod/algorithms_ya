# Самое длинное слово
# Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному менеджменту.
# Так как Гоша хочет спланировать день заранее, ему необходимо оценить сложность статьи.
# Он придумал такой метод оценки: берётся случайное предложение из текста и в нём ищется 
# самое длинное слово. Его длина и будет условной сложностью статьи.
# Помогите Гоше справиться с этой задачей.


def get_longest_word(line: str) -> str:
    max_word = ''
    word = ''
    for char in line:
        if ord(char) != 32:
            word += char
        else:
            word = ''

        if len(word) > len(max_word):
            max_word = word
    return max_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))
    

print_result(get_longest_word(read_input()))
