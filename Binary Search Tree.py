#!/usr/bin/env python
# coding: utf-8

# # BST without duplicates

# In[ ]:


class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value):
        if self.data == value:
            return 
        elif value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BST(value)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def sort(self):
        sorted_val = []
        if self.right:
            sorted_val += self.right.sort()

        sorted_val.append(self.data)

        if self.left:
            sorted_val += self.left.sort()

        return sorted_val

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
                
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)  
            
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right            


            min_val = self.right.find_min()
            self.data = min_val
            self.right.delete(min_val)

        return self

def build_tree(vector):
    temp = BST(vector[0])
    for index in range(1,len(vector)):
        temp.add_child(vector[index])
    return temp


# # BST with duplicates

# In[19]:


class BST:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.middle = None

    def add_child(self,data):
        if self.data == data:
            if self.middle:
                self.middle.add_child(data)
            else:
                self.middle = BST(data)
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def sort_elements(self):
        elements = []
        if self.left:
            elements += self.left.sort_elements()
        if self.middle:
            elements += self.middle.sort_elements()
        elements.append(self.data)
        if self.right:
            elements += self.right.sort_elements()

        return elements
    
#     def count_duplicate(self, data):
#         if data < self.data:
#             return self.left.count_duplicate(data)
#         elif data > self.data:
#             return self.right.count_duplicate(data)
#         else:
#             count = 0
#             if self.middle is None:
#                 return count
#             else:
#                 while self.middle:
#                     print(count)
#                     count += 1
#                     self = self.middle
#                 return count
            
    def count_duplicate(self):
        count = 0
        if self.middle is None:
            return count
        else:
            while self.middle:
                count += 1
                self = self.middle
            return count
            
    def find_min(self, duplicate_search = False):
        if self.left is None:
            if duplicate_search:
                return self.data, self.count_duplicate()
            else:
                return self.data
        else:
            return self.left.find_min(duplicate_search = duplicate_search)
            
    def find_max(self, duplicate_search = False):
        if self.right in None:
            if duplicate_search:
                return self.data, self.count_duplicate()
            else:
                return self.data
        else:
            return self.right.find_max(duplicate_search = duplicate_search)            
                
    
    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val, duplicate_count = self.right.find_min(duplicate_search = True)
            print(min_val, duplicate_count)
            self.data = min_val
            self.right.delete(min_val)
            if duplicate_count != 0:
                self.middle = BST(min_val)
                for _ in range(duplicate_count-1):
                    self.middle.add_child(min_val)

                
        return self
                
                

def build_tree(vector):
    temp = BST(vector[0])
    for index in range(1,len(vector)):
        temp.add_child(vector[index])
    return temp


# In[20]:


import random
# del T
random.seed(10)
A = random.choices(list(range(-10,10)),k=40)
print(A)
T = build_tree(A)
print(T.sort_elements())
T.delete(3)
print(T.sort_elements())

