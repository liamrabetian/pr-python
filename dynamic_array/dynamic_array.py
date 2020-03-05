import ctypes


class DynamicArray():
    """Implementation of dynamic array in python."""
    
    def __init__(self):
        self.count = 0 # Count of actual elements in array
        self.capacity = 1 # Default capacity of an array
        self.List_A = self._make_array(self.capacity)
    
    def __len__(self):
        # Return length of array
        return self.count
    
    def __getitem__(self, index):
        # Return element at index k
        if not 0 <= index < self.count:
            return IndexError('Index Is Out Of Bounds')
        return self.List_A[index]
    
    def append(self, element):
        # Add element to end of array
        if self.count == self.capacity:
            self._resize(2*self.capacity)
        
        self.List_A[self.count] = element
        self.count += 1
    
    def _resize(self, new_capacity):
        # resize array, 2 times existing array by convention
        List_B = self._make_array(new_capacity)

        for index in range(self.count):
            List_B[index] = self.List_A[index]
        
        self.List_A = List_B
        self.capacity = new_capacity
    
    def _make_array(self, capacity):
        # Make a raw array
        return (capacity * ctypes.py_object)()
    

if __name__ == '__main__':
    # just test the class
    arr = DynamicArray()
    arr.append(1)
    arr.append(4)
    print('length of the array is: ', len(arr))
    print('second index of array is: ', arr[1])
