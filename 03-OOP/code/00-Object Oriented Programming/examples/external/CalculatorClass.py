class Calculator:
    """
	Hello world
	"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def summ(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        if self.y == 0:
            return 'cant divide on zero'
        return self.x / self.y

