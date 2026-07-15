class Vector:

    def __init__(self, l):
        self.l  = l


    def __len__(self):  #ye length nikalne k liye use hone wala method
        return len(self.l)

s = Vector([2,3,4])
print(len(s))