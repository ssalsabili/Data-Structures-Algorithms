# # BST with duplicates
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
                
                

def build_tree_WD(vector):
    temp = BST(vector[0])
    for index in range(1,len(vector)):
        temp.add_child(vector[index])
    return temp