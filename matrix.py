from random import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        
        for i in range(self.rows):
            self.data.append([])
            for j in range(self.cols):
                self.data[i].append(0)
    
    @staticmethod
    def multiply(matrix1, matrix2):
        if not matrix1.cols == matrix2.rows:
            print('Cannot multiply two matrices where cols of a do not equal rows of b in number')
            return
        result_mat = Matrix(matrix1.rows, matrix2.cols)
        for i in range(result_mat.rows):
            for j in range(result_mat.cols):
                sum = 0
                for k in range(matrix1.cols):
                    sum += matrix1.data[i][k] * matrix2.data[k][j]
                result_mat.data[i][j] = sum
                
        return result_mat
        
    def scale(self, item):
        if isinstance(item, int) or isinstance(item, float):
            self._scalar_scale(item)
        elif isinstance(item, Matrix):
            self._matrix_scale(item)
            
    def _scalar_scale(self, n):
        # [[int(y) for y in x] for x in values]
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n
                
    def _matrix_scale(self, other_matrix):
        if not other_matrix.rows == self.rows or not other_matrix.cols == self.cols:
            print('Matrices need to be of the same dimensions to element wise add')
            return
        # [[int(y) for y in x] for x in values]
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= other_matrix.data[i][j]
                
    def add(self, item):
        if isinstance(item, int) or isinstance(item, float):
            self._scalar_add(item)
        elif isinstance(item, Matrix):
            self._matrix_add(item)
            
    def _scalar_add(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += n
                
    def _matrix_add(self, other_matrix):
        if not other_matrix.rows == self.rows or not other_matrix.cols == self.cols:
            print('Matrices need to be of the same dimensions to element wise add')
            return
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += other_matrix.data[i][j]
                
    @staticmethod
    def subtract(a,b):
        #element wise substraction
        if not a.rows == b.rows or not a.cols == b.cols:
            print('Rows and columns of two matrices must match.')
            raise ValueError
        result_mat = Matrix(a.rows, a.cols)
        for i in range(result_mat.rows):
            for j in range(result_mat.cols):
                result_mat.data[i][j] = a.data[i][j] - b.data[i][j] 
        return result_mat
    
    def transpose(self):
        result_mat = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result_mat.data[j][i] = self.data[i][j]        
        self.data = result_mat.data
        self.rows = result_mat.rows
        self.cols = result_mat.cols
    
    @staticmethod     
    def static_transpose(m):
        result_mat = Matrix(m.cols, m.rows)
        for i in range(m.rows):
            for j in range(m.cols):
                result_mat.data[j][i] = m.data[i][j]
        return result_mat
    
    @staticmethod
    def from_array(arr):
        res = Matrix(len(arr), 1)
        for i in range(len(arr)):
            res.data[i][0] = arr[i]
        return res
    
    def to_array(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr
        
    @staticmethod
    def static_to_array(m):
        arr = []
        for i in range(m.rows):
            for j in range(m.cols):
                arr.append(m.data[i][j])
        return arr
        
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random() * 2 - 1
                
    def apply_func(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])
                
    @staticmethod        
    def static_apply_func(m, func):
        result = Matrix(m.rows, m.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = func(m.data[i][j])
        return result
                
    
    def __str__(self):
        str_represent = []
        for r in range(self.rows):
            str_represent.append(str(self.data[r]))
        return '\n'.join(str_represent)
