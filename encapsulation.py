class Protected:
    def __init__(self):
        self.__privateVar = 23
        
    def prntPrivate (self):
        print (self.__privateVar)

    def declarePrivate (self, private):
        self.__privateVar = private

obj = Protected()
obj.prntPrivate()
obj.declarePrivate(24)
obj.prntPrivate()
