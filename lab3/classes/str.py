class up:
    def _init(self):
        self.str = ""
    def getString(self):
        self.str = input("Enter a string: ")
    def printString(self):
        print(self.str.upper())

a = up()

a.getString()

a.printString()