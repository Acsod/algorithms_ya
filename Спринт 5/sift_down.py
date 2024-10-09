# Просеивание вниз
# Напишите функцию, совершающую просеивание вниз в куче на максимум. Гарантируется, 
# что порядок элементов в куче может быть нарушен только элементом, от которого 
# запускается просеивание.
# Функция принимает в качестве аргументов массив, в котором хранятся элементы кучи,
# и индекс элемента, от которого надо сделать просеивание вниз. Функция должна вернуть 
# индекс, на котором элемент оказался после просеивания. Также необходимо изменить 
# порядок элементов в переданном в функцию массиве.
# Индексация в массиве, содержащем кучу, начинается с единицы. Таким образом, сыновья
# вершины на позиции v это 2v и 2v+1. Обратите внимание, что нулевой элемент в 
# передаваемом массиве фиктивный, вершина кучи соответствует 1-му элементу.


def sift_down(heap, idx) -> int:

    heap_max_index = len(heap) - 1
    left = idx * 2
    right = idx * 2 + 1

    if left > heap_max_index:
        return idx
    
    if right <= heap_max_index and heap[right] > heap[left]:
        index_largest = right
    else:
        index_largest = left

    if heap[index_largest] > heap[idx]:
        heap[index_largest], heap[idx] = heap[idx], heap[index_largest]
        return sift_down(heap, index_largest)

    return idx

            
def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
    