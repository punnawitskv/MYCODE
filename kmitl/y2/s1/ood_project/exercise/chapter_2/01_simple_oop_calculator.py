class Calculator:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return self.num + other.num
    
    def __sub__(self, other):
        return self.num - other.num
    
    def __mul__(self, other):
        return self.num * other.num
    
    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Division by zero is undefined.")
        return self.num / other.num

x, y = input("Enter num1 num2 : ").split(",")
x_calc = Calculator(int(x))
y_calc = Calculator(int(y))

print(x_calc.__add__(y_calc))
print(x_calc.__sub__(y_calc))
print(x_calc.__mul__(y_calc))
print(x_calc.__truediv__(y_calc))
