# IB Computer Science Collection Tools

class Arrays:
    def __init__(self, d_type, size):
        self.__data = [None for _ in range(size)]
        self.__d_type = d_type
        self.__size = 0
        self.__max_size = size
    # end of init

    def __str__(self):
        if self.__size == 0:
            return "[]"
        else:
            result = "["
            for i in range(self.__size):
                if i < self.__size - 1:
                    result += str(self.__data[i]) + ", "
                else:
                    result += str(self.__data[i])
            result += "]"
            
            return result
    # end of __str__()
    def __repr__(self):
        return self.__str__()
    # end of __repr__()

    def __getitem__(self, i):
        if i >= self.__size:
            raise IndexError(f"Index {i} goes beyond the size of the Array.")
        elif i < 0:
            raise IndexError("Arrays object has no negative index.")
        else:
            return self.__data[i]

    def append(self, value):
        if self.__size == self.__max_size:
            raise Exception("The Arrays is full and cannot take anymore data.")
        elif isinstance(value, self.__d_type):
            self.__data[self.__size] = value
            self.__size += 1
        else:
            raise TypeError(f"{value} does not match the data type of the object.")
# end of Arrays

class Collections:
    def __init__(self):
        self.__data = []
        self.__i = 0
    
    def isEmpty(self):
        return len(self.__data) == 0
    
    def addItem(self, value):
        self.__data.append(value)
    
    def getNext(self):
        if self.__i >= len(self.__data):
            raise IndexError("No more values in the collection")
            return None
        answer = self.__data[self.__i]
        self.__i += 1
        return answer
    
    def hasNext(self):
        return self.__i < len(self.__data)
    
    def resetNext(self):
        self.__i = 0

    def __str__(self):
        if self.isEmpty():
            return "[]"
        else:
            result = "["
            for i in range(len(self.__data)):
                if i < len(self.__data) - 1:
                    result += str(self.__data[i]) + ", "
                else:
                    result += str(self.__data[i])
            result += "]"
            
            return result
    # end of __str__()
    def __repr__(self):
        return self.__str__()
    # end of __repr__()
