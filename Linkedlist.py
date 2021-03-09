#!/usr/bin/env python
# coding: utf-8

# # Linked list

# In[3]:


class Node:
    def __init__(self, data = None, next_element = None):
        self.data = data
        self.next_element = next_element
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_elements(self):
        itr = self.head
        if itr is None:
            print("Linked list is empty!")
            return
        lstr = ''
        while itr:
            lstr += str(itr.data) + '==>' if itr.next_element else str(itr.data)
            itr = itr.next_element
        print(lstr)
        
    def get_length(self):
        L = 0
        itr = self.head
        while itr:
            L += 1
            itr = itr.next_element
        return L
    
    def insert_begin(self, data):
        temp = Node(data, self.head)
        self.head = temp
        
    def insert_end(self, data):
        itr = self.head
        if itr is None:
            self.insert_begin(data)
            return
        
        while itr.next_element:
            itr = itr.next_element
            
        itr.next_element = Node(data)
        
    def insert_at(self, data, index):
        L = self.get_length()
        if index < 0 or index > L:
            print("invalid index!")
            return 
        
        if index == 0:
            self.insert_begin(data)
            return
            
        if index == L:
            self.insert_end(data)
            return
        
        count = 0
        itr = self.head
        while 1:
            if count == index - 1:
                itr.next_element = Node(data, itr.next_element)
                return
            itr = itr.next_element
            count += 1
            
    def remove_at(self, index):
        L = self.get_length()
        if index < 0 or index > L:
            print("invalid index!")
            return
        
        if L == 0:
            print("The list is empty!")
            return
        
        if index == 0:
            self.head = itr.head.next_element
            return
        
        count = 0
        itr = self.head
        while 1:
            if count == index - 1:
                itr.next_element = itr.next_element.next_element
                return
            count += 1
            itr = itr.next_element 
            
    def insert_after_value(self, comp, data):
        itr = self.head
        if itr is None:
            self.head = self.insert_begin(data)
            return
        
        while itr:
            if itr.data == comp:
                itr.next_element = Node(data, itr.next_element)
                return
            itr = itr.next_element
        print("Value not found!")
        
    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next_element
            return
        temp = itr
        itr = itr.next_element
        while itr:
            if itr.data == data:
                temp.next_element = itr.next_element
                return
            temp = itr
            itr = itr.next_element
        print("Value not found!")
    def build_Linkedlist(self, vec):
        L = len(vec)
        for index in range(L):
            self.insert_end(vec[index])
            
        


# In[24]:


ll = LinkedList()
ll.build_Linkedlist(["banana","mango","grapes","orange"])
ll.print_elements()
ll.insert_at("blueberry",1)
ll.print_elements()
ll.remove_at(2)
ll.print_elements()


# In[4]:


ll = LinkedList()
ll.build_Linkedlist(["banana","mango","grapes","orange"])
ll.print_elements()
print("#1")
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print_elements()
print("#2")
ll.remove_by_value("orange") # remove orange from linked list
ll.print_elements()
print("#3")
ll.remove_by_value("figs")
ll.print_elements()
print("#4")
ll.remove_by_value("banana")
ll.print_elements()
print("#x")
ll.remove_by_value("mango")
ll.print_elements()
print("#x")
ll.remove_by_value("apple")
ll.print_elements()
print("#x")
ll.remove_by_value("grapes")
ll.print_elements()
print("#5")


# # Doubly Linked list

# In[27]:


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


# In[28]:


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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



