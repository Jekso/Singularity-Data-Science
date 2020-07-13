class Circle:
    """
	Circle Class
    """
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        
    def getCircumference(self):
        return self.radius * self.pi * 2
    
    def getArea(self):
        return self.radius * self.radius * self.pi

