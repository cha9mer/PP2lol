#cheres class sdelat upper 
class StringHandler:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
a = StringHandler()
a.getString()
a.printString()