class Location:
    def __init__(self, x, y):
        self.lat = float(x)
        self.lng = float(y)

    def distance(self, a, b):
        dist = pow(((pow((self.lat - float(a)), 2) + pow(
            (self.lng - float(b)), 2))), 0.5)
        return dist


class Parking:
    def __init__(self, x, y):
        self.location = Location(x, y)
        self.taken = False

    def resereve(self):
        self.taken = True


class User:
    def __init__(self, x, y, radius):
        self.location = Location(x, y)
        self.radius = float(radius)


# class Max_Heap:
#     def __init__(self, items=[]):
#         self.heap = [None]
#         for i in items:
#             self.push(i)
#
#     def push(self, data):
#         self.heap.append(data)
#         self.__float_up(len(self.heap) - 1)
#
#     def pop(self):
#         if len(
#                 self.heap
#         ) > 2:  #it means if there are more elements in it apart from None
#             self.__swap(1, len(self.heap) - 1)
#             max_data = self.heap.pop()
#             self.__bubble_down(1)
#         elif len(
#                 self.heap
#         ) == 2:  #it means if there is on element in it apart from None
#             max_data = self.heap.pop()
#         else:
#             return None, "Empty Heap!"
#         return max_data
#
#     def __swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#
#     def __float_up(self, index):
#         parent == index // 2
#         if index <= 1:
#             return
#         elif self.heap[index] > self.heap[parent]:
#             self.__swap(index, parent)
#             self.__float_up(parent)
#
#     def __bubble_down(self, index):
#         left, right = index * 2, index * 2 + 1
#         largest = index
#         if len(self.heap) > left and self.heap[largest] < self.heap[left]:
#             largest = left
#         if len(self.heap) > right and self.heap[largest] < self.heap[right]:
#             largest = right
#         if largest != index:
#             self.__swap(index, largest)
#             self.__bubble_down(largest)
