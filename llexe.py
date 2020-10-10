# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class Linked_list:
#     def __init__(self):
#         self.head = None

    # def insert_begining(self,data):
    #     node = Node(data, self.head)
    #     self.head = node
    #
    # def print_list(self):
    #     if self.head is None:
    #         print("The linked list is empty. ")
    #         return

    #     current = self.head
    #     string = ""
    #     while current != None:
    #         string += str(current.data) + "-->"
    #         current = current.next
    #
    #     print(string)
    #
    # def insert_end(self,data):
    #     if self.head is None:
    #         self.head = Node(data, None)
    #         return
    #
    #     current = self.head
    #     while current.next != None:
    #         current = current.next
    #
    #     current.next = Node(data,None)

    # def insert_values(self, data_list):
    #     self.head = None
    #     for data in data_list:
    #         self.insert_end(data)
    #
    # def get_length(self):
    #     count = 0
    #     current = self.head
    #     while current != None:
    #         count += 1
    #         current = current.next
    #     return count
    #
    # def remove_at(self,index):
    #     if index < 0 or index >= self.get_length():
    #         raise Exception ("The index is invalid")
    #     if index == 0:
    #         self.head = self.head.next
    #         return

    #     current = self.head
    #     count = 0
    #     while current.next != None:
    #         if count == index-1:
    #             current.next = current.next.next
    #             break
    #         current = current.next
    #         count += 1
    #
    # def insert_at(self,index,data):
    #     if index < 0 or index >= self.get_length():
    #         raise Exception ("The index is invalid")
    #     if index == 0:
    #         self.insert_begining(data)
    #
    #     current = self.head
    #     count = 0
    #     while current.next != None:
    #         if count == index-1:
    #             node = Node(data, current.next)
    #             current.next = node
    #             break
    #         current = current.next
    #         count += 1
    #
    # def insert_after_value(self, data_after, data_to_insert ):
    #     if self.head is None:
    #         return
    #
    #     if self.head.data == data_after:
    #         node = Node(data_to_insert,self.head.next)
    #
    #     current = self.head
    #     while current != None:
    #         if current.data == data_after:
    #             node = Node(data_to_insert, current.next)
    #             current.next = node
    #         current = current.next
    #
    #
    # def remove_by_value(self,data):
    #     if self.head is None:
    #         return
    #
    #     if self.head.data == data:
    #         self.head = self.head.next
    #         return
    #
    #     current = self.head
    #     while current.next != None:
    #         if current.next.data == data:
    #             current.next = current.next.next
    #         current = current.next
    #
    # def get_last_node(self):
    #     current = self.head
    #     while current.next != None:
    #         current = current.next
    #
    #     return current


# Implementing a double linked list
class Node:
    def __init__(self, data=None, next= None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Linked_list:
    def __init__(self):
        self.head = None

    
    def get_last_node(self):
        current = self.head
        while current != None:
            current = current.next

        return current
     
    def print_forward(self):
        if self.head is None:
            print("The linked list is empty.")

        current = self.head
        empty = ""
        while current.next != None:
            empty += str(current.data) + "-->"
            current = current.next

        print(empty)

    def print_back(self):
        if self.head is None:
            print("The list is empty")
            return

        current = self.get_last_node() 
        empty = ""
        while current:
            empty += current.data + "-->"
            current = current.prev

        print("The linked list printed backwards:", empty)


    # def insert_begining(self,data):
    #     node = Node(data, self.head, None)
    #     self.head.prev = node
    #     self.head = node

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = Node(data,None,current)
        


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
           self.insert_end(data)
        



        
           











# gl = Linked_list()
# gl.insert_at_begining(5)
# gl.insert_at_begining(6)
# gl.insert_at_begining(7)
# gl.insert_at_begining(8)
# gl.print_forward()
# gl.print_back()

ll = Linked_list()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print_forward()
ll.print_back()
# ll.get_last_node()
# # ll.remove_by_value("grapes")
# # ll.insert_after_value("banana","apple")
# ll.print_list()


# il = Linked_list()
# il.insert_end(5)
# il.insert_end(6)
# il.insert_end(7)
# il.insert_end(8)
# il.insert_at(0,7)
# # il.remove_at(0)
# print("The count is:", il.get_length())
# il.print_list()
