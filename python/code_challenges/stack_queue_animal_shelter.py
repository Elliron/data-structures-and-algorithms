class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self, pref):
        if self.isEmpty():
            return
        find_pet = True
        while find_pet == True:
            if self.front.value != pref:
                temp = self.front
                self.front = temp.next

                if (self.front == None):
                    self.rear = None
            else:
                find_pet = False

    def __str__(self):
        string = ""
        current = self.front
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

if __name__== '__main__':
    q = AnimalShelter()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    print("Queue Front " + str(q.front.value))
    print("Queue Rear " + str(q.rear.value))


# class AnimalShelter:
#     def __init__(self, front= None, back= None):
#         self.front = front
#         self.back = back
#         self.size = 0

#     def __str__(self):
#         string = ""
#         current = self.front
#         while current is not None:
#             string += f"{ {current.value} } ->"
#             current = current.next
#         string += f" None "
#         return string

#     def __len__(self):
#         return self.size

#     def is_empty(self):
#         if self.size == 0:
#             return True
#         else:
#             return False

#     def enqueue(self, front):
#         new = self.Node(front, None)
#         if self.is_empty():
#             self.front = new
#         else:
#             self.back.next = new
#         self.back = new
#         self.size +=1

#     def dequeue (self, pref):
#         waiting_area = ()
#         if self.is_empty():
#             raise Exception("empty")
#         result = self.front.value
#         for result in AnimalShelter:
#             if pref != "dog".upper() or pref != "cat".upper():
#                 return None
#             elif result != pref.upper():
#                 waiting_area.push(result)
#             elif result == pref.upper():
#                 AnimalShelter.enqueue(waiting_area)
#                 return result
#         self.front = self.front.next
#         self.size -= 1

#         if self.is_empty():
#             self.back = None
#         return result


# if __name__ =='__main__':

#     shelter = AnimalShelter()
#     shelter.enqueue(Node('dog'))
#     shelter.enqueue(Node('dog'))
#     shelter.enqueue(Node('cat'))
#     shelter.enqueue(Node('dog'))
#     shelter.enqueue(Node('dog'))
#     entire_list = str(shelter)
#     print(entire_list)
