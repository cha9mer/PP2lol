class Circle:
    def __init__ (self,x):
        self.x = x
    def radius(self):
        result = self.x**2* 3.14159
        return result
n=int(input())
object = Circle(n)
area = object.radius()
print(f"{area:.2f}")