class Matrix:

    def __init__(self, list):
        self.matrix = list
    
    def vals(self):
        return self.matrix

    def dims(self):
        return len(self.matrix),len(self.matrix[0])

    def is_symetric(self):
        symmetry = True

        if(len(self.matrix[0]) != len(self.matrix)):
            symmetry =  False
        else:
            for i in range(len(self.matrix)):
                for ii in range(len(self.matrix)):
                    if(self.matrix[i][ii] != self.matrix[ii][i]):
                        symmetry = False  
        
        return symmetry


    def __add__(x, y):

        product = []
        for i in range(len(x.matrix)):
            product.append([])
            for ii in range(len(x.matrix[0])):
                product[i].append(x.matrix[i][ii] + y.matrix[i][ii])

        return Matrix(product)

    def __sub__(x, y):

        product = []
        for i in range(len(x.matrix)):
            product.append([])
            for ii in range(len(x.matrix[0])):
                product[i].append(x.matrix[i][ii] - y.matrix[i][ii])

        return Matrix(product)


    def __mul__(x, y):
        product = []
        num_ab = 0

        if(isinstance(y, Matrix)):
            for i in range(len(x.matrix)):
                product.append([])
                for ii in range(len(y.matrix[0])):
                    for k in range(len(x.matrix[0])):
                        num_ab += (x.matrix[i][k] * y.matrix[k][ii])
                    product[i].append(num_ab)
                    num_ab = 0
        else:
            for i in range(len(x.matrix)):
                product.append([])
                for ii in range(len(x.matrix[0])):
                    product[i].append(x.matrix[i][ii]*y)
        
        return Matrix(product)


    def zero_matrix(r, c):
        return Matrix([[0]*c]*r) 

    def identity_matrix(n):
        id = []
        for i in range(n):
            id.append([])
            for ii in range(n):
                if(i == ii):
                    id[i].append(1)
                else:
                    id[i].append(0)
                    
        return Matrix(id)


    @staticmethod
    def write(mat):
        list = mat.matrix
        string = ""

        for row in list:
            for num in row:
                string += str(num) + ' '
            string = string.strip()
            string += '\n'
        
        return string.strip()


