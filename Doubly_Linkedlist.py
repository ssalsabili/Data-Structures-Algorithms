# # Doubly Linked list
class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
class Doubly_LinkedList:
    def __init__(self, head = None, end = None):
        self.head = head
    
    def get_length(self):
        itr = self.head
        L = 0
        while itr:
            L += 1
            itr = itr.right
        
        return L
    
    def insert_begin(self, data):
        self.head = Node(data, left = None, right = self.head)
        
    
    def insert_end(self, data):
        itr = self.head
        if itr is None:
            self.insert_begin(data)
        else:
            while itr.right:
                itr = itr.right
            itr.right = Node(data, left = itr, right = None)
    
    def insert_at(self, index, data):
        L = self.get_length()
        if index < 0 or index > L:
            print('Index is not valid!')
            return
        
        if index == 0:
            self.insert_begin(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.right = Node(data, left = itr, right = itr.right)
                return
            count += 1
            itr = itr.right   
    
    def remove_at(self, index):
        L = self.get_length()
        if index < 0 or index > L:
            print('Index is not valid!')
            return
        
        if L == 0:
            print("Linked list is empty")
            return
        
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.right = itr.right.right
                return
            count += 1
            itr = itr.right

    
    def insert_after_value(self, comp, data):
        itr = self.head
        if itr.data == comp:
            itr.right = Node
        while itr:
            if comp == itr.data:
                itr.right = Node(data, left = itr, right = itr.right)
                return
            itr = itr.right
        print("value not found!")
    
    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if data == itr.data:
                itr = itr.left
                itr.right = itr.right.right
                return
            itr = itr.right
        print("value not found!")
    
    def print_forward(self):
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '==>' if itr.right else str(itr.data)
            itr = itr.right
        print(lstr)
    
    def print_backward(self):
        itr = self.head
        lstr = ''
        while itr.right:
            itr = itr.right
        while itr:
            lstr += itr.data + '==>' if itr.left else str(itr.data)
            itr = itr.left
        print(lstr)
    
    def build_Linkedlist(self, vec):
        self.head = None
        for index in range(len(vec)):
            self.insert_end(vec[index])

if __name__ == '__main__':

    ll = Doubly_LinkedList()
    ll.build_Linkedlist(["banana","mango","grapes","orange"])
    print(ll.get_length())
    ll.print_forward()
    ll.print_backward()
    ll.insert_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
