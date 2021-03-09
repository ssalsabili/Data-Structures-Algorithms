# # BST without duplicates
class BST_without_duplicates:
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

def build_tree_WOD(vector):
    temp = BST_without_duplicates(vector[0])
    for index in range(1,len(vector)):
        temp.add_child(vector[index])
    return temp


if __name__ == '__main__':

    import random
    # del T
    random.seed(10)
    A = random.choices(list(range(-10,10)),k=40)
    print(A)
    T = build_tree_WD(A)
    print(T.sort_elements())
    T.delete(3)
    print(T.sort_elements())

