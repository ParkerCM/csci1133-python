import math

class Point():
    def __init__(self, xval=0, yval=0):
        self.__xval = xval
        self.__yval = yval
    def __add__(left, right):
        xsum = left.__xval + right.__xval
        ysum = left.__yval + right.__yval
        return Point(xsum, ysum)
    def __eq__(self, other):
        if self.__xval == other.__xval:
            if self.__yval == other.__yval:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return '('+str(self.__xval)+','+str(self.__yval)+')'
    
        
    
class Complex:

    def __init__(self, real=0.0,imag=0.0):
        self.__real = real
        self.__imag = imag

    def __str__(self):
        if self.__imag == 0.0:
            return str(self.__real)
        elif self.__imag < 0.0:
            return str(self.__real)+' - ' + str(abs(self.__imag)) + 'i'
        else:
            return str(self.__real)+' + ' + str(self.__imag) + 'i'

    def __repr__(self):
        if self.__imag == 0.0:
            return str(self.__real)
        elif self.__imag < 0.0:
            return str(self.__real)+' - ' + str(abs(self.__imag)) + 'i'
        else:
            return str(self.__real)+' + ' + str(self.__imag) + 'i'

    def setReal(self, real):
        self.__real = real

    def setImag(self, imag):
        self.__imag = imag

    def getReal(self):
        return self.__real

    def getImag(self):
        return self.__imag

    def __add__(left, right):
        x = left.__real + right.__real
        y = left.__imag + right.__imag
        return Complex(x, y)
    def __neg__(self):
        return Complex(self.__real, self.__imag * -1)
    def __mul__(self, other):
        a = (self.__real * other.__real)
        b = (self.__real * other.__imag) 
        c = (self.__imag * other.__real)
        d = (self.__imag * other.__imag)
        d *= -1
        e = a + d
        f = b + c
        return Complex(e, f)
        


def roots(a,b,c):
    x1 = Complex()
    x2 = Complex()

    if a < 0:
        return Complex(-b/(2*a), 0.0)
    else:
        x1 = Complex(-b/(2*a), math.sqrt(abs(b**2 - (4*a*c)))/(2*a))
        x2 = Complex(-b/(2*a), -(math.sqrt(abs(b**2 - (4*a*c)))/(2*a)))
        return x1, x2
        


def mandelbrot(z0, n):
    mandlist=[z0]
    count = 1
    comp = z0
    var = z0
    
    while count < n:
        comp = var * var
        
        var = z0 + comp
        mandlist.append(var)
        count += 1
    
    return mandlist


class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = matrix
    def __str__(self):
        row = 0
        col = 0
        string = ''
        while row < len(self.matrix):
            while col < len(self.matrix[0]):
                string+=str(self.matrix[row][col])
                string += ' '
                col +=1
            row+=1
            col = 0
            string+='\n'
        return string








    
    
    
        
