class Calculator:
    """
    Calculator Class
    """
    @staticmethod
    def summ(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y
    
    @staticmethod
    def mul(x, y):
        return x * y
    
    @staticmethod
    def div(x, y):
        if y == 0:
            return 'Cant divide on zero'
        else:
            return x / y